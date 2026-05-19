from transformers import pipeline
from app.retrieval.search import search

# Use stable task supported across versions
llm = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    max_new_tokens=256)


def build_context(results, max_chars=3000):
    context = []
    total = 0

    for r in results:
        block = f"SOURCE: {r['source']}\n{r['text']}\n"

        if total + len(block) > max_chars:
            break

        context.append(block)
        total += len(block)

    return "\n---\n".join(context)


def ask(question: str):
    results = search(question, top_k=5)
    context = build_context(results)

    prompt = f"""
You are Mnemosyne, a precise AI that answers using Obsidian notes.

Rules:
- You are a retrieval-only assistant.

Rules:
- Answer ONLY using provided context
- If context is insufficient, say "Not found in notes"
- Do not add general knowledge
- Do not explain concepts unless present in notes
- Prefer bullet points extracted from notes
- Do NOT repeat the prompt
- Summarize clearly in bullet points if needed

QUESTION:
{question}

CONTEXT:
{context}

ANSWER:
"""

    output = llm(prompt, max_new_tokens=256, do_sample=False)

    return output[0]["generated_text"]