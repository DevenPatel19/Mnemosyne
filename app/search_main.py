import sys
from app.retrieval.search import search
from dotenv import load_dotenv
load_dotenv()


def main():
    if len(sys.argv) < 2:
        print('Usage: python -m app.search_main "your query"')
        return

    query = sys.argv[1]

    print(f"\nSearching: {query}\n")

    results = search(query)

    for i, r in enumerate(results, 1):
        print(f"Result {i}")
        print(f"Score: {r['score']:.4f}")
        print(f"Source: {r['source']}")
        print(f"Text: {r['text'][:300]}")
        print("-" * 60)


if __name__ == "__main__":
    main()