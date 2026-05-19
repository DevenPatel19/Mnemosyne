I built the ingestion layer of a RAG system that recursively scans and parses my Obsidian knowledge vault, extracts markdown content and metadata, and prepares documents for downstream semantic embedding and vector retrieval workflows using Pinecone.

## Why We Need Embeddings

### LLMs do NOT inherently “remember” your Obsidian vault.

#### Instead:

- notes are converted into vectors
- vectors represent semantic meaning
- Pinecone stores those vectors
- queries are embedded the same way
- nearest semantic matches are retrieved

#### Meaning:

“How do distributed systems scale?”
can retrieve notes even if exact wording differs.


## Next Phase

Next we’ll build:

## Intelligent Ingestion Pipeline

Including:

- semantic chunking
- metadata extraction
- wikilink parsing
- tag extraction
- LangChain document objects
- embedding generation
- Pinecone vector uploads