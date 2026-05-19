from pathlib import Path

from langchain_core.documents import Document

from app.ingest.markdown_parser import (
    extract_frontmatter,
    extract_tags,
    extract_wikilinks
)

from app.ingest.chunker import create_text_splitter


def load_obsidian_vault(vault_path: str):
    vault = Path(vault_path)

    if not vault.exists():
        raise FileNotFoundError(f"Vault path does not exist: {vault_path}")

    markdown_files = list(vault.rglob("*.md"))

    splitter = create_text_splitter()

    documents = []

    for file_path in markdown_files:

        try:
            raw_content = file_path.read_text(encoding="utf-8")

            # -----------------------------
            # Metadata Extraction
            # -----------------------------

            frontmatter, clean_content = extract_frontmatter(raw_content)

            wikilinks = extract_wikilinks(clean_content)

            tags = extract_tags(clean_content)

            # -----------------------------
            # Chunking
            # -----------------------------

            chunks = splitter.split_text(clean_content)

            # -----------------------------
            # Build LangChain Documents
            # -----------------------------

            for chunk in chunks:

                doc = Document(
                    page_content=chunk,
                    metadata={
                        "source": str(file_path),
                        "file_name": file_path.name,
                        "tags": tags,
                        "wikilinks": wikilinks,
                        **frontmatter
                    }
                )

                documents.append(doc)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    return documents