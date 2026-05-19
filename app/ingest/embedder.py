from sentence_transformers import SentenceTransformer

# Load lightweight embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Convert text chunks into embeddings locally (no API required).
    """

    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings.tolist()


"""_summary_
from sentence_transformers import SentenceTransformer

# Load lightweight embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts: list[str]) -> list[list[float]]:
"""
#  Convert text chunks into embeddings locally (no API required).
"""

    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings.tolist()
"""

# import os
# from openai import OpenAI


# def get_client():
#     return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# def embed_texts(texts: list[str]) -> list[list[float]]:
#     """
#     Convert text chunks into embeddings using OpenAI.
#     """

#     client = get_client()

#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=texts
#     )

#     return [item.embedding for item in response.data]