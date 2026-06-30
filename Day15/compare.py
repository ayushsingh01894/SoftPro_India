from sentence_transformers import SentenceTransformer, util

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