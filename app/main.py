from dotenv import load_dotenv
import os
from pinecone import Pinecone

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=api_key)

indexes = pc.list_indexes()

print("Mnemosyne initialized.")
print("Pinecone Connected.")
print("Indexes:", indexes)
print("Target Index:", index_name)