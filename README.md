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

- Web UI (e.g. Streamlit)
- Expose as an API (FastAPI or Flask)
