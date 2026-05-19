import sys
from app.chat.qa_engine import ask


def main():
    if len(sys.argv) < 2:
        print('Usage: python -m app.chat_main "your question"')
        return

    question = sys.argv[1]

    print("\n🧠 Mnemosyne Thinking...\n")

    answer = ask(question)

    print("ANSWER:\n")
    print(answer)


if __name__ == "__main__":
    main()