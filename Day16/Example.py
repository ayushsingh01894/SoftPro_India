from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # sentence ="I love Ai"
    # vector = model.encode(sentence)
    # print(vector.shape)
    # print(vector)

    sentence = [
        "The cat set on a mat",
        " A feline rested on the rug ",
        "intrest rates rose this quarter"
    ]
    vector = model.encode(sentence)
    # print(vector.shape)
    query = input("Enter your query: ")
    query_vector = model.encode(query)
    scores = cos_sim(query_vector, vector)
    print("Similarity Scores:")
    print(scores)
    # best_index = scores.argmax()
    # print("\nBest Match:")
    # print(sentence[best_index])

if __name__ == "__main__":
    main()

# =================================================================================

DOCS = [
    " A car is a four wheeled vehicle for the road",
    "An automobile takes you from place to place ",
    "The chef cooked a delicious pasta dinner",
    "Photosynthesis lets plants make food from light"
]
QUERY = "How does a motor vehicle works?"

def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vector = model.encode(QUERY)
    docs_vector = model.encode(DOCS)
    scores = util.cos_sim(query_vector, docs_vector)[0]
    print(scores)

if __name__ == "__main__":
    main()


