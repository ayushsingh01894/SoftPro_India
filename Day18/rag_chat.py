from pathlib import Path
import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"
MODEL_NAME = "llama-3.3-70b-versatile"

def retrieve_context(collection, embedder, question: str, k: int = 2):
    query_embedding = embedder.encode(question).tolist()
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    matches =[]
    for document, metadata, distance in zip(
        result["documents"][0],
        result["metadatas"][0],
        result["distances"][0],
    ):
        matches.append(
            {
                "document":document,
                "topic":metadata.get("topic"),
                "distence":distance,
                "similarity": 1- distance,            
            }
        )
    return matches

def build_context_block(matches)-> str:
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

def main()-> None:
    load_dotenv()
    llm = Groq()

    chroma_client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = chroma_client.get_collection(COLLECTION_NAME)
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    print("="* 72)
    print("RAG chat over your saved notes")
    print("=" * 72)
    print("Ask a question about the notes. Type 'quit' to exit.")

    while True:
        question = input("\n You :").strip()
        if not question:
            continue
        if question.lower() in { "quit" ,"exit"}:
            print("Bye !")
            break
        matches = retrieve_context(collection, embedder, question, k=2)
        context_block = build_context_block(matches)
        answer = ask_groq(llm, question, context_block)

        print("\n Retrieved context :")
        for match in matches:
            print(
                f" -[{match['topic']}] similarity ={match['similarity']:.3f}"
                f"{match['document']}"
            )

        print(f"\nAssistant: {answer}")

if __name__ == "__main__":
    main()








"""

 DOCUMENT INGESTION

PDF / Word / Excel / Website
              │
              ▼
      Document Loader
              │
              ▼
        Text Chunking
              │
              ▼
     Embedding Model
(all-MiniLM-L6-v2, BGE, e5)
              │
              ▼
       Vector Database
     (ChromaDB, Qdrant)
              │
────────────────────────────────────

            USER QUERY
              │
              ▼
     User asks a question
              │
              ▼
      Query Embedding
              │
              ▼
     Similarity Search
              │
              ▼
     Top-K Relevant Chunks
              │
              ▼
       Prompt Builder
              │
              ▼
      LLM (Groq/OpenAI)
              │
              ▼
         Final Answer

"""