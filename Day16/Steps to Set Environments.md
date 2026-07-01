python -m venv venv
venv\Scripts\activate
python Chat_bot.py

# Installation
pip install sentence-transformers

Program 1 — Load Model
# --------------------------------------
# Import SentenceTransformer
# --------------------------------------
from sentence_transformers import SentenceTransformer
# --------------------------------------
# Load Embedding Model
# --------------------------------------
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
print("Model Loaded Successfully")

# Program 2 — Generate One Embedding
from sentence_transformers import SentenceTransformer
# Load model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
# Sentence
sentence = "Python is a programming language."
# Generate embedding
embedding = model.encode(sentence)
print(embedding)
# check demention = print(len(embedding))

Output
[ 0.034
 -0.118
  0.224
 ...
]

# Program 4 — Multiple Sentences


from sentence_transformers import SentenceTransformer
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
sentences = [
    "Python is easy.",
    "Machine Learning is part of AI.",
    "SQL stores data.",
    "Football has 11 players."
]
embeddings = model.encode(sentences)
print(embeddings.shape)

# Real Pipeline
PDF
↓
Chunking
↓
SentenceTransformer
↓
Embeddings
↓
FAISS
↓
Search