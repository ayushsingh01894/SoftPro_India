"""
Day 18 - Step 1: Store note embeddings in a persistent Chroma collection.
"""

# `Path` helps us build reliable folder paths relative to this file.
from pathlib import Path

# Chroma is the local vector database we use to save and retrieve vectors.
import chromadb
# SentenceTransformer gives us a local embedding model: text -> vector.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points to the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` is where Chroma will save its database files on disk.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` is the logical table-like name inside Chroma.
COLLECTION_NAME = "student_notes"

# These are the notes we want to embed and store.
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
    # Load the local embedding model used throughout this day.
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Pull out only the raw note text because that is what we embed.
    documents = [note["document"] for note in NOTES]
    # Convert every note into a vector, then convert numpy arrays to plain Python lists for Chroma.
    embeddings = model.encode(documents).tolist()

    # Open a persistent Chroma client so data is saved inside `DB_DIR`.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Create the collection if it does not exist, or reuse it if it already exists.
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        # Tell Chroma to treat distance as cosine distance for vector search.
        metadata={"hnsw:space": "cosine"},
    )

    # Upsert means "insert new rows or overwrite existing rows with the same ids".
    collection.upsert(
        # Stable ids let us update the same note later if needed.
        ids=[note["id"] for note in NOTES],
        # These are the actual text documents we want to retrieve later.
        documents=documents,
        # Metadata travels with each vector so we can display or filter by topic later.
        metadatas=[{"topic": note["topic"]} for note in NOTES],
        # These are the embedding vectors for each document.
        embeddings=embeddings,
    )

    # Print a small status summary so students can see what got stored.
    print("=" * 72)
    print("Saved note vectors to Chroma")
    print("=" * 72)
    print(f"Database folder : {DB_DIR}")
    print(f"Collection name : {COLLECTION_NAME}")
    print(f"Stored records  : {collection.count()}")

    # Print every stored note so students can match ids/topics to documents.
    print("\nStored notes:")
    for note in NOTES:
        print(f"- {note['id']} [{note['topic']}] {note['document']}")


# Run `main()` only when this file is executed directly.
if __name__ == "__main__":
    main()

# Reload_collection.py
# ------------------------------------------------------------------------------------
"""
Day 18 - Step 2: Reload the saved Chroma collection in a fresh script.
"""

# `Path` lets us point back to the same database folder used in step 1.
from pathlib import Path

# Chroma is the database we are reconnecting to.
import chromadb


# `BASE_DIR` is the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` must match step 1, otherwise we would open a different database.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` must also match the collection created earlier.
COLLECTION_NAME = "student_notes"


def main() -> None:
    # Open the saved Chroma database from disk.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Reconnect to the existing collection by name.
    collection = client.get_collection(COLLECTION_NAME)
    # Fetch stored ids, documents, and metadata so we can inspect what survived.
    snapshot = collection.get(include=["documents", "metadatas"])

    # Print a small summary showing that the database reopened successfully.
    print("=" * 72)
    print("Reloaded Chroma collection from disk")
    print("=" * 72)
    print(f"Database folder : {DB_DIR}")
    print(f"Collection name : {COLLECTION_NAME}")
    print(f"Stored records  : {collection.count()}")

    # Print each saved record to prove the vectors/documents persisted across runs.
    print("\nSnapshot:")
    for doc_id, metadata, document in zip(
        snapshot["ids"],
        snapshot["metadatas"],
        snapshot["documents"],
    ):
        # Use a fallback topic just in case metadata is missing.
        topic = metadata.get("topic", "unknown")
        print(f"- {doc_id} [{topic}] {document}")


# Run this script only when executed directly.
if __name__ == "__main__":
    main()

#---------------------------------------------------------
"""
Day 18 - Step 3: Retrieve the nearest notes from Chroma.
"""

# `Path` is used to find the shared database folder.
from pathlib import Path

# Chroma stores and searches our saved note vectors.
import chromadb
# SentenceTransformer embeds the user's query before we search.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points to the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` points to the same persistent database folder created in step 1.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` is the saved note collection we want to query.
COLLECTION_NAME = "student_notes"

# These are sample natural-language questions we will test against the notes.
QUERIES = [
    "How do I make a prompt more specific?",
    "What does binary search require first?",
    "How do recursive functions stop?",
]


def print_matches(collection, model, query: str, k: int = 2) -> None:
    # Convert the query text into one embedding vector.
    query_embedding = model.encode(query).tolist()
    # Ask Chroma for the top `k` nearest documents to that query vector.
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        # We ask Chroma to return the matched documents, metadata, and distances.
        include=["documents", "metadatas", "distances"],
    )

    # Print the query before its ranked matches.
    print(f"\nQuery: {query}")
    # Walk through the returned parallel lists one rank at a time.
    for rank, (document, metadata, distance) in enumerate(
        zip(
            result["documents"][0],
            result["metadatas"][0],
            result["distances"][0],
        ),
        start=1,
    ):
        # Convert cosine distance into an easy-to-read similarity-like score.
        similarity = 1 - distance
        print(
            f"{rank}. similarity={similarity:.3f} topic={metadata.get('topic', 'unknown')} "
            f"-> {document}"
        )


def main() -> None:
    # Re-open the saved database.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Re-open the collection containing the stored notes.
    collection = client.get_collection(COLLECTION_NAME)
    # Load the same embedding model so query vectors live in the same vector space as the notes.
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Print a heading for the retrieval demo.
    print("=" * 72)
    print("Nearest-note retrieval with Chroma")
    print("=" * 72)

    # Run several sample queries so students can see retrieval behavior.
    for query in QUERIES:
        print_matches(collection, model, query)


# Run this module only when the file is executed directly.
if __name__ == "__main__":
    main()

#----------------------------------------------------------
""" 
we need to run first store_vector.py
then run python rag_chat.py
Before running we need to install ( pip install chromadb sentence-transformers torch python-dotenv groq)

Day 18 - Step 4: Retrieve notes from Chroma, then answer with Groq.
"""

# `Path` helps us locate the saved local database folder.
from pathlib import Path

# Chroma handles storage and nearest-neighbor retrieval.
import chromadb
# `load_dotenv` loads the `GROQ_API_KEY` from a local `.env` file.
from dotenv import load_dotenv
# `Groq` is the hosted chat client we use for the final answer.
from groq import Groq
# SentenceTransformer converts the user's question into an embedding vector.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points at the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` points to the Chroma folder created in earlier steps.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` identifies the note collection inside Chroma.
COLLECTION_NAME = "student_notes"
# `MODEL_NAME` is the Groq chat model used to generate the final answer.
MODEL_NAME = "llama-3.3-70b-versatile"


def retrieve_context(collection, embedder, question: str, k: int = 2):
    # Embed the user's question so we can search by meaning instead of keywords.
    query_embedding = embedder.encode(question).tolist()
    # Retrieve the nearest `k` notes from Chroma.
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        # We want the note text, metadata, and distance scores back.
        include=["documents", "metadatas", "distances"],
    )

    # Normalize Chroma's nested response into a simpler list of match dictionaries.
    matches = []
    for document, metadata, distance in zip(
        result["documents"][0],
        result["metadatas"][0],
        result["distances"][0],
    ):
        matches.append(
            {
                # The raw note text that was retrieved.
                "document": document,
                # The note topic stored as metadata.
                "topic": metadata.get("topic", "unknown"),
                # The raw cosine distance returned by Chroma.
                "distance": distance,
                # A friendlier similarity-like score for display.
                "similarity": 1 - distance,
            }
        )
    return matches


def build_context_block(matches) -> str:
    # Build one text block that will be inserted into the LLM prompt.
    lines = []
    for index, match in enumerate(matches, start=1):
        lines.append(
            f"[Source {index} | topic={match['topic']} | similarity={match['similarity']:.3f}] "
            f"{match['document']}"
        )
    # Join each retrieved note with a newline so the prompt stays readable.
    return "\n".join(lines)


def ask_groq(client: Groq, question: str, context_block: str) -> str:
    # Send the retrieved notes and user question to the chat model.
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                # The system message tells the model to stay grounded in the notes.
                "content": (
                    "You answer only from the retrieved notes. If the notes are not enough, say "
                    "'I do not have enough notes to answer that confidently.' Keep answers short."
                ),
            },
            {
                "role": "user",
                # The user message contains both the retrieved context and the question.
                "content": f"Retrieved notes:\n{context_block}\n\nQuestion: {question}",
            },
        ],
        # Low temperature keeps the answer stable and less creative.
        temperature=0.2,
    )
    # Return the text content of the first model choice.
    return response.choices[0].message.content or ""


def main() -> None:
    # Load the Groq API key from `.env`.
    load_dotenv()
    # Create the Groq chat client.
    llm = Groq()
    # Re-open the saved Chroma database.
    chroma_client = chromadb.PersistentClient(path=str(DB_DIR))
    # Re-open the note collection inside that database.
    collection = chroma_client.get_collection(COLLECTION_NAME)
    # Load the local embedding model for query embeddings.
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    # Print a heading so the terminal session is easy to recognize.
    print("=" * 72)
    print("RAG chat over your saved notes")
    print("=" * 72)
    print("Ask a question about the notes. Type 'quit' to exit.")

    # Keep the chat session running until the user quits.
    while True:
        # Read one question from the terminal.
        question = input("\nYou: ").strip()
        # Skip empty input so we do not send blank prompts.
        if not question:
            continue
        # Exit the loop on common quit commands.
        if question.lower() in {"quit", "exit"}:
            print("Bye.")
            break

        # Retrieve the top matching notes for the question.
        matches = retrieve_context(collection, embedder, question, k=2)
        # Convert those matches into a single prompt context block.
        context_block = build_context_block(matches)
        # Ask the chat model to answer using only that retrieved context.
        answer = ask_groq(llm, question, context_block)

        # Show the user exactly which notes were retrieved.
        print("\nRetrieved context:")
        for match in matches:
            print(
                f"- [{match['topic']}] similarity={match['similarity']:.3f} "
                f"{match['document']}"
            )

        # Print the grounded answer from the model.
        print(f"\nAssistant: {answer}")


# Run the chat loop only when this file is executed directly.
if __name__ == "__main__":
    main()
