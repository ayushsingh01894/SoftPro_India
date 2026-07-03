from pathlib import Path
import chromadb
BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"


def main() -> None:
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_collection(COLLECTION_NAME)
    snapshot = collection.get(include=["documents", "metadatas"])
    print(snapshot)
    for doc_id, metadata,document in zip(
        snapshot["ids"],
        snapshot["metadatas"],
        snapshot["documents"],
    ):
        topic = metadata.get("topic")
        print(f"- {doc_id} [{topic}] {document}")
        
if __name__ == "__main__":
    main()        