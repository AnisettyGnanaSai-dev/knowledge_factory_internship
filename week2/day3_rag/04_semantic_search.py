from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ---------------------------------------------------
# SAMPLE DOCUMENT CHUNKS
# ---------------------------------------------------

documents = [

    "Employees may claim up to ₹18,000 per quarter for travel reimbursement.",

    "Medical insurance is provided after 6 months of employment.",

    "The cafeteria is open from 9 AM to 8 PM.",

    "Python is widely used for machine learning applications.",

    "Annual bonuses are based on employee performance reviews."
]

# ---------------------------------------------------
# LOAD EMBEDDING MODEL
# ---------------------------------------------------

print("=" * 60)
print("LOADING MODEL")
print("=" * 60)

try:
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("[OK] Embedding model loaded")

except Exception as e:
    print(f"[ERROR] Failed to load model: {e}")
    exit()

# ---------------------------------------------------
# GENERATE DOCUMENT EMBEDDINGS
# ---------------------------------------------------

print("\n" + "=" * 60)
print("GENERATING DOCUMENT EMBEDDINGS")
print("=" * 60)

document_embeddings = model.encode(documents)

print(f"\nTotal documents embedded: {len(documents)}")

# ---------------------------------------------------
# USER QUERY
# ---------------------------------------------------

query = "What is the travel reimbursement limit?"

print("\n" + "=" * 60)
print("USER QUERY")
print("=" * 60)

print(f"\nQuery: {query}")

# ---------------------------------------------------
# QUERY EMBEDDING
# ---------------------------------------------------

query_embedding = model.encode([query])

# ---------------------------------------------------
# COSINE SIMILARITY
# ---------------------------------------------------

similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

# ---------------------------------------------------
# GET TOP MATCHES
# ---------------------------------------------------

top_k = 3

top_indices = np.argsort(similarities)[::-1][:top_k]

print("\n" + "=" * 60)
print("TOP MATCHING DOCUMENTS")
print("=" * 60)

for rank, index in enumerate(top_indices, start=1):

    print(f"\nRank #{rank}")

    print(f"Document: {documents[index]}")

    print(f"Similarity Score: {similarities[index]:.4f}")

# ---------------------------------------------------
# KEYWORD SEARCH COMPARISON
# ---------------------------------------------------

print("\n" + "=" * 60)
print("KEYWORD SEARCH COMPARISON")
print("=" * 60)

keyword = "reimbursement"

for doc in documents:

    if keyword.lower() in doc.lower():

        print(f"\nKeyword Match Found:")
        print(doc)