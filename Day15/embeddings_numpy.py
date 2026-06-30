"""
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence = "I love AI"
embedding = model.encode(sentence)

# Save to a NumPy file
np.save("embedding.npy", embedding)

print("Embedding saved!")

"""
import numpy as np

embeddings = np.load("embeddings.npy")

print(embeddings)
print(len(embeddings))