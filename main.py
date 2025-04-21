import sys
from retriever import retrieve_context
from pokemon_agent import PokemonTrainer


def main():
    if len(sys.argv) < 2:
        print("Please provide a question.")
        print("Usage: python main.py 'Your question here'")
        return

    question = " ".join(sys.argv[1:])
    context = retrieve_context(question)

    trainer = PokemonTrainer()
    answer = trainer.ask(question, context)

    print("\n📄 Context Used:\n", context)
    print("\n🤖 Answer:\n", answer)


if __name__ == "__main__":
    main()
