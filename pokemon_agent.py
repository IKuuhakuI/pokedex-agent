from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate


class PokemonTrainer:
    """
    An agent powered by an LLM to answer Pokémon-related questions using provided context.
    """

    def __init__(
        self,
        model_name: str = "llama3",
        base_url: str = "http://localhost:11434",
    ):
        self.llm = OllamaLLM(model=model_name, base_url=base_url)

        self.prompt = PromptTemplate.from_template(
            "You are a helpful Pokédex assistant named Ziul.\n"
            "Wheneved asked, start with: Professor Ziul here! And after taht, answer the following question using only the context below.\n\n"
            "Context:\n{context}\n\n"
            "Question:\n{question}"
        )

        self.chain = self.prompt | self.llm

    def ask(self, question: str, context: str) -> str:
        """
        Ask the PokémonTrainer a question using provided context.
        """
        try:
            return self.chain.invoke({"context": context, "question": question}).strip()
        except Exception as e:
            print(f"❌ PokemonTrainer error: {e}")
            return "[Error] LLM failed to respond."
