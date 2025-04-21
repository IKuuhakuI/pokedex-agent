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


def retrieve_context(query: str) -> str:
    """
    Retrieve the top 3 most relevant Pokémon entries based on semantic similarity to the query.
    """
    data_path = Path(__file__).parent / "data" / "sample_data.json"

    with open(data_path, "r", encoding="utf-8") as file:
        pokemon_data = json.load(file)

    flattened_entries = [build_pokemon_context(entry) for entry in pokemon_data]

    entry_embeddings = (
        embedding_model.encode(flattened_entries, convert_to_tensor=True).cpu().numpy()
    )
    query_embedding = (
        embedding_model.encode([query], convert_to_tensor=True).cpu().numpy()
    )

    similarity_scores = cosine_similarity(query_embedding, entry_embeddings)[0]
    top_indices = np.argsort(similarity_scores)[::-1][:3]

    top_matches = [flattened_entries[i] for i in top_indices]
    return "\n\n".join(top_matches)
