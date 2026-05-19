from pathlib import Path

"""
    What This Does
Path.rglob("*.md")

Recursively finds:

all markdown files
inside nested folders too

Exactly how Obsidian vaults are structured.
    """

def load_obsidian_vault(vault_path: str):
    vault = Path(vault_path)

    if not vault.exists():
        raise FileNotFoundError(f"Vault path does not exist: {vault_path}")

    markdown_files = list(vault.rglob("*.md"))

    documents = []

    for file_path in markdown_files:
        try:
            content = file_path.read_text(encoding="utf-8")

            documents.append({
                "file_name": file_path.name,
                "path": str(file_path),
                "content": content
            })

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    return documents