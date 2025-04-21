from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory


class PokemonTrainer:
    """
    An LLM-powered agent that can hold short Pokémon conversations.
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
            "{chat_history}\nHuman: {question}\nAI:"
        )

        self.memory = InMemoryChatMessageHistory()

        self.chain = RunnableWithMessageHistory(
            self.prompt | self.llm,
            input_messages_key="question",
            history_messages_key="chat_history",
            get_session_history=lambda session_id: self.memory,
        )

    def ask(
        self,
        context: str,
        question: str,
        session_id: str = "default",
    ) -> str:
        """
        Ask a question with memory context. A session_id can scope memory.
        """
        try:
            return self.chain.invoke(
                {
                    "context": context,
                    "question": question,
                },
                config={"configurable": {"session_id": session_id}},
            ).strip()

        except Exception as e:
            print(f"Memory-enabled agent error: {e}")
            return "[Error] LLM failed."
