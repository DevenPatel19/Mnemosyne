import os
from sentence_transformers import SentenceTransformer
from app.retrieval.vector_store import get_index

# Load model (same as ingestion)
model = SentenceTransformer("all-MiniLM-L6-v2")


def search(query: str, top_k: int = 5):
    """
    Semantic search over Obsidian vault via Pinecone.
    """

    # 1. Embed query
    query_embedding = model.encode(query).tolist()

    # 2. Connect to Pinecone
    index = get_index()

    # 3. Query vector DB
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    # 4. Format results
    matches = []

    for match in results["matches"]:
        matches.append({
            "score": match["score"],
            "text": match["metadata"].get("text", ""),
            "source": match["metadata"].get("source", "")
        })

    return matches