GROQ_MODELS = [
    "llama-3.1-8b-instant",       # fast + cheap, great default
    "llama-3.3-70b-versatile",    # smarter, a little slower
    "openai/gpt-oss-20b",         # a different model family to compare
]

DEFAULT_TEMPERATURE = 0.2
DEFAULT_MAX_TOKENS = 512
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE_WORDS = 120
CHUNK_OVERLAP_WORDS = 20
TOP_K = 4                         # how many chunks to retrieve per question
COLLECTION_NAME = "uploaded_docs"


SYSTEM_PROMPT = (
    "You are a helpful assistant that answers questions about the user's uploaded "
    "documents. Answer ONLY using the context provided below. If the context does "
    "not contain the answer, say: 'I couldn't find that in your documents.' "
    "Be concise and, where useful, mention which source the answer came from."
)