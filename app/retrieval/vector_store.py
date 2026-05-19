import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()


def get_index():
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")

    pc = Pinecone(api_key=api_key)
    return pc.Index(index_name)