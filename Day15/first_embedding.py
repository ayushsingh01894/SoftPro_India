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
    best_index = scores.argmax()
    print("\nBest Match:")
    print(sentence[best_index])

if __name__ == "__main__":
    main()

