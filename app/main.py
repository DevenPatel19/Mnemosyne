from dotenv import load_dotenv
import os
import sys

from pinecone import Pinecone
from app.ingest.vault_loader import load_obsidian_vault

load_dotenv()

# -----------------------------
# Pinecone Setup
# -----------------------------

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=api_key)

print("Mnemosyne initialized.")
print("Pinecone Connected.")
print()

# -----------------------------
# Vault Path Input
# -----------------------------

if len(sys.argv) < 2:
    print("Usage:")
    print(r'python app/main.py "C:\Path\To\Vault"')
    sys.exit(1)

vault_path = sys.argv[1]

print(f"Loading vault: {vault_path}")
print()

# -----------------------------
# Load Vault
# -----------------------------

documents = load_obsidian_vault(vault_path)

print(f"Loaded {len(documents)} markdown files.")
print()

# Preview first few files

print(f"Generated {len(documents)} semantic chunks.")
print()

for doc in documents[:3]:

    print("CONTENT:")
    print(doc.page_content[:300])

    print()

    print("METADATA:")
    print(doc.metadata)

    print("-" * 60)