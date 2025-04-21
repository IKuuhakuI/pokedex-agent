# 🧠 Pokédex AI Assistant

A conversational Pokémon assistant that answers natural language questions using a local LLM (via Ollama) and semantic search over a Pokémon dataset. Built for the **AI Agent Developer Technical Test**.

## 🚀 Features

- Accepts natural language questions via CLI
- Vector-based context retrieval using sentence-transformers
- Uses Ollama (`llama3`) locally for responses
- Memory-enabled: supports follow-up questions
- Cleanly structured and easy to extend

## 🛠️ Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/IKuuhakuI/pokedex-ai-agent.git
cd pokedex-ai-agent
```

### 2. Install `uv` (if not already)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Install and run Ollama (LLM backend)

```bash
curl -fsSL https://ollama.com/install.sh | sh

ollama pull llama3

ollama serve
```

## 🧪 How to Use

```bash
uv run python main.py
```

Then interact with the assistant:

```
🧑 You: Tell me about Bulbasaur
🤖 LLM: Bulbasaur is a Grass/Poison-type Pokémon...

🧑 You: And its evolution?
🤖 LLM: It evolves into Ivysaur at level 16...
```

To exit, type `exit` or `quit`.

## 📁 Project Structure

```
ai-agent/
├── data/
│   └── sample_data.json       # Pokémon knowledge base
├── retriever.py               # Vector similarity context retriever
├── pokemon_agent.py           # Memory-enabled LangChain agent
├── main.py                    # CLI entrypoint
├── requirements.txt           # Dependencies
└── README.md
```

## 📌 Requirements

- Python 3.10+
- Ollama with llama3 or similar model
- Local machine with enough RAM for Ollama

## 🧠 Ideas for Improvement

- Web UI
- Expose as an API (FastAPI or Flask)
- A Graph based search for better entities and relationships context
- The possibility of the user uploading his own data (pdf, url or any other), with, for example, a book with histories about pokemon. Based on that, I'd create my own data for context building.

# As for what I'd do if I had more time:

1. Unit tests. This is the core of any project for me. So I'd test it a lot.
2. A better file structure organization. I find the way I've done it now to be a bit messy.
3. A GraphRag approach. The project itself was really fun, so I'd say a GraphRag would complement the second source a lot. I could try to link pokemons to their moves and have an even better context.
4. A bigger history. I tried to stick with a small history for demonstration purposes. But I'd love to try and challenge a bigger one.
5. An UI. This one is self explanatory, this kind of project really shines with it.
6. A separate AI layer. I'd make all AI calls more abstract. That way, I could always change from Ollama to OpenAi, Claude,... without the need to rewrite a lot of code.
7. Code pattern. I'd create a project with strict code pattern rules. I used Ruff as my linter, but I'd make it as the project default. Also would add pre-commit/pre-push rules to ensure code follows the pattern and all tests are working.
8. Abstraction of Agents. I'd create a protocol that would make it easier to create new agents, not only guaranteeing the code pattern, but also would add the possibility of user custom agents.
9. The possibility of the user uploading context (url, pdfs, etc...) to build the context.

Those are the 9 points I'd enhance if given more time!

# As for a summary on my approach:

- Context Retriever: Uses sentence transformers and cosine similarity to rank and select top-matching context entries.
- Conversational Agent: A memory-limited LangChain agent powered by llama3 through langchain_ollama, using strict prompts to ensure answers are grounded and relevant to the context.
- Short-term Memory: It remembers the last chat interaction.
- Multi-source support: Integrates multiple dataset to enable reasoning over both pokemon and their movesets.
- Interactive CLI: Allows real-time user interaction with natural assistant-like experience.
