from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ---------------------------------------------------
# LOAD EMBEDDING MODEL
# ---------------------------------------------------

print("=" * 60)
print("LOADING EMBEDDING MODEL")
print("=" * 60)

try:
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("[OK] Model loaded successfully")

except Exception as e:
    print(f"[ERROR] Failed to load model: {e}")
    exit()

# ---------------------------------------------------
# SAMPLE SENTENCES
# ---------------------------------------------------

sentences = [

    "The doctor treated the patient",

    "A physician helped the sick person",

    "Pizza tastes amazing with cheese",

    "Travel reimbursement limit is ₹18,000"
]

# ---------------------------------------------------
# GENERATE EMBEDDINGS
# ---------------------------------------------------

print("\n" + "=" * 60)
print("GENERATING EMBEDDINGS")
print("=" * 60)

embeddings = model.encode(sentences)

print(f"\nEmbedding shape: {embeddings.shape}")

print("\nFirst 10 dimensions of first embedding:\n")

print(embeddings[0][:10])

# ---------------------------------------------------
# COSINE SIMILARITY
# ---------------------------------------------------

print("\n" + "=" * 60)
print("COSINE SIMILARITY MATRIX")
print("=" * 60)

similarity_matrix = cosine_similarity(embeddings)

# Print matrix neatly
for i in range(len(sentences)):

    print(f"\nSentence: {sentences[i]}")

    for j in range(len(sentences)):

        similarity_score = similarity_matrix[i][j]

        print(
            f"  Similarity with sentence {j+1}: "
            f"{similarity_score:.4f}"
        )

# ---------------------------------------------------
# QUERY SEARCH DEMO
# ---------------------------------------------------

query = "What is the reimbursement amount?"

print("\n" + "=" * 60)
print("QUERY SEARCH")
print("=" * 60)

query_embedding = model.encode([query])

query_similarity = cosine_similarity(
    query_embedding,
    embeddings
)

best_match_index = np.argmax(query_similarity)

print(f"\nQuery: {query}")

print(
    f"\nBest matching sentence:\n"
    f"{sentences[best_match_index]}"
)

print(
    f"\nSimilarity score: "
    f"{query_similarity[0][best_match_index]:.4f}"
)   