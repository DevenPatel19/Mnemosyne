import os
import sys
import uuid

from dotenv import load_dotenv
load_dotenv()

from pinecone import Pinecone

from app.ingest.vault_loader import load_obsidian_vault
from app.ingest.embedder import embed_texts
from app.retrieval.vector_store import upsert_vectors


# -----------------------------
# CLI / Interactive Input
# -----------------------------

if len(sys.argv) > 1:
    vault_path = sys.argv[1]
else:
    vault_path = input("Enter your Obsidian vault path: ").strip().strip('"')

print("Mnemosyne initialized.")
print("Pinecone Connected.\n")

print(f"Loading vault: {vault_path}\n")


# -----------------------------
# Load Vault
# -----------------------------

documents = load_obsidian_vault(vault_path)

print(f"Loaded {len(documents)} markdown chunks.\n")


# -----------------------------
# Embedding Step
# -----------------------------

print("Embedding chunks...")
# texts = [doc.page_content for doc in documents]  # commented out due to no billing structure in open ai account
MAX_CHUNKS = 20  # safe testing limit
texts = [doc.page_content for doc in documents[:MAX_CHUNKS]]
documents = documents[:MAX_CHUNKS]
# embeddings = embed_texts(texts)           # commented out due to no billing structure in open ai account

print(f"Embedding {len(texts)} chunks (TEST MODE)...")

embeddings = embed_texts(texts)

print(f"Generated {len(embeddings)} embeddings.\n")


# -----------------------------
# Build Pinecone Vectors
# -----------------------------

vectors = []

for doc, embedding in zip(documents, embeddings):
    vectors.append({
        "id": str(uuid.uuid4()),
        "values": embedding,
        "metadata": {
            **doc.metadata,
            "text": doc.page_content
        }
    })


# -----------------------------
# Upload to Pinecone
# -----------------------------

print("Uploading to Pinecone...")

upsert_vectors(vectors)

print("Upload complete.\n")


# -----------------------------
# Debug Preview
# -----------------------------

print("Preview of indexed chunks:\n")

for doc in documents[:3]:

    print("CONTENT:")
    print(doc.page_content[:300])
    print()

    print("METADATA:")
    print(doc.metadata)
    print("-" * 60)