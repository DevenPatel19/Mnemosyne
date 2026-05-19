import os
from pinecone import Pinecone


def get_index():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index_name = os.getenv("PINECONE_INDEX_NAME")

    return pc.Index(index_name)


def upsert_vectors(vectors):
    index = get_index()
    index.upsert(vectors=vectors)