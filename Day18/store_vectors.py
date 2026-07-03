# We need to install - pip install sentence-transformers chromadb groq torch python-dotenv 

from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"

NOTES = [
    {
        "id": "note-1",
        "topic": "algorithms",
        "document": "Binary search only works on sorted data. Check the middle and discard half each step.",
    },
    {
        "id": "note-2",
        "topic": "python",
        "document": "Use a dictionary when you need fast key lookup instead of scanning a full list.",
    },
    {
        "id": "note-3",
        "topic": "prompting",
        "document": "Good prompts include the role, task, constraints, and the output format you want.",
    },
    {
        "id": "note-4",
        "topic": "recursion",
        "document": "Recursion needs a base case and a smaller subproblem so the calls eventually stop.",
    },
]

def main() -> None:
    model = SentenceTransformer("all-MiniLM-L6-V2")
    documents = [note["document"] for note in NOTES]
    embeddings = model.encode(documents).tolist()
    client = chromadb.PersistentClient(path=str(DB_DIR))

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space":"cosine"},
    )
    collection.upsert(
        ids=[note["id"] for note in NOTES],

        documents=documents,
        metadatas=[{"topic": note["topic"]}for note in NOTES],
        embeddings=embeddings,
    )
    print(f"Stored records : {collection.count()}")

if __name__ == "__main__":
    main()
