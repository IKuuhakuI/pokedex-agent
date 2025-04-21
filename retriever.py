import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def build_pokemon_context(entry: dict) -> str:
    """
    Create a flattened string representation of a Pokémon's data for vector embedding.
    """
    name = entry.get("name", {}).get("english", "Unknown")
    types = ", ".join(entry.get("type", []))
    stats = entry.get("base", {})
    evolution = entry.get("evolution", {}).get("next", [])
    next_evolution = (
        ", ".join([f"#{e[0]} at {e[1]}" for e in evolution]) if evolution else "None"
    )

    lines = [
        f"{name} is a {types} type Pokémon.",
        f"Description: {entry.get('description', 'No description available.')}",
        f"Species: {entry.get('species', 'Unknown')}",
        f"Base stats: {', '.join(f'{k}: {v}' for k, v in stats.items()) or 'Unknown'}",
        f"Next evolution: {next_evolution}",
    ]

    return "\n".join(lines)


def build_move_context(entry: dict) -> str:
    """
    Create a text description of a move entry.
    """
    name = entry.get("ename", "Unknown")
    move_type = entry.get("type", "Unknown")
    power = entry.get("power", "N/A")
    accuracy = entry.get("accuracy", "N/A")
    pp = entry.get("pp", "N/A")
    category = entry.get("category", "Unknown")

    return (
        f"{name} is a {move_type}-type move ({category}). "
        f"It has {power} power, {accuracy}% accuracy, and {pp} PP."
    )


def retrieve_context(query: str) -> str:
    """
    Retrieve the top 3 most relevant Pokémon or move entries based on semantic similarity to the query.
    """
    base_path = Path(__file__).parent / "data"

    flattened_entries = []

    with open(base_path / "sample_data.json", encoding="utf-8") as f:
        pokemon_data = json.load(f)
        flattened_entries += [build_pokemon_context(p) for p in pokemon_data]

    with open(base_path / "moves.json", encoding="utf-8") as f:
        moves_data = json.load(f)
        flattened_entries += [build_move_context(m) for m in moves_data]

    entry_embeddings = (
        embedding_model.encode(flattened_entries, convert_to_tensor=True).cpu().numpy()
    )
    query_embedding = (
        embedding_model.encode([query], convert_to_tensor=True).cpu().numpy()
    )

    scores = cosine_similarity(query_embedding, entry_embeddings)[0]
    top_indices = np.argsort(scores)[::-1][:3]

    return "\n\n".join(flattened_entries[i] for i in top_indices)
