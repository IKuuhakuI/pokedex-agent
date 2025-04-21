from retriever import retrieve_context
from pokemon_agent import PokemonTrainer


def main():
    trainer = PokemonTrainer()

    print("🧠 Welcome to the Pokédex Assistant!")
    print("Ask me anything about Pokémon. Type 'exit' to quit.\n")

    while True:
        question = input("🧑 You: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        context = retrieve_context(question)

        answer = trainer.ask(question=question, context=context)
        print(f"🤖 LLM: {answer}\n")


if __name__ == "__main__":
    main()
