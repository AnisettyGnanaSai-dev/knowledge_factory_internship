import fitz
import numpy as np
from pathlib import Path

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

import ollama

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

PDF_PATH = BASE_DIR / "data" / "sample.pdf"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

TOP_K = 3

MODEL_NAME = "qwen2.5:7b"

# ---------------------------------------------------
# LOAD EMBEDDING MODEL
# ---------------------------------------------------

print("=" * 60)
print("LOADING EMBEDDING MODEL")
print("=" * 60)

try:
    embedding_model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    print("[OK] Embedding model loaded")

except Exception as e:
    print(f"[ERROR] Failed to load embedding model: {e}")
    exit()

# ---------------------------------------------------
# EXTRACT TEXT FROM PDF
# ---------------------------------------------------

def extract_text_from_pdf(pdf_path):

    full_text = []

    try:
        doc = fitz.open(pdf_path)

        for page in doc:

            text = page.get_text()

            if text:
                full_text.append(text)

        doc.close()

        return "\n".join(full_text)

    except Exception as e:
        print(f"[ERROR] PDF extraction failed: {e}")
        return ""

# ---------------------------------------------------
# CHUNKING WITH OVERLAP
# ---------------------------------------------------

def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

# ---------------------------------------------------
# CREATE EMBEDDINGS
# ---------------------------------------------------

def create_embeddings(chunks):

    return embedding_model.encode(chunks)

# ---------------------------------------------------
# RETRIEVE RELEVANT CHUNKS
# ---------------------------------------------------

def retrieve_relevant_chunks(
    query,
    chunks,
    chunk_embeddings,
    top_k=3
):

    # Embed user query
    query_embedding = embedding_model.encode([query])

    # Compute cosine similarity
    similarities = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    # Top matching chunks
    top_indices = np.argsort(similarities)[::-1][:top_k]

    retrieved_chunks = []

    for index in top_indices:

        retrieved_chunks.append({
            "chunk": chunks[index],
            "score": similarities[index]
        })

    return retrieved_chunks

# ---------------------------------------------------
# GENERATE RESPONSE USING OLLAMA
# ---------------------------------------------------

def generate_rag_answer(query, retrieved_chunks):

    context = "\n\n".join([
        chunk["chunk"]
        for chunk in retrieved_chunks
    ])

    prompt = f"""
Answer the question based ONLY on the context below.

If the answer is not in the context,
say "I don't know."

Context:
{context}

Question:
{query}
"""

    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"[ERROR] Ollama generation failed: {e}"

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

def main():

    print("\n" + "=" * 60)
    print("FULL RAG PIPELINE")
    print("=" * 60)

    # ---------------------------------------------------
    # STEP 1: EXTRACT TEXT
    # ---------------------------------------------------

    text = extract_text_from_pdf(PDF_PATH)

    if not text:
        print("[ERROR] No text extracted")
        return

    print(f"\n[OK] Extracted {len(text)} characters")

    # ---------------------------------------------------
    # STEP 2: CHUNK TEXT
    # ---------------------------------------------------

    chunks = chunk_text(
        text,
        CHUNK_SIZE,
        CHUNK_OVERLAP
    )

    print(f"[OK] Created {len(chunks)} chunks")

    # ---------------------------------------------------
    # STEP 3: CREATE EMBEDDINGS
    # ---------------------------------------------------

    chunk_embeddings = create_embeddings(chunks)

    print(f"[OK] Generated embeddings")

    # ---------------------------------------------------
    # STEP 4: USER QUERY
    # ---------------------------------------------------

    query = input("\nEnter your question: ")

    # ---------------------------------------------------
    # STEP 5: RETRIEVE CHUNKS
    # ---------------------------------------------------

    retrieved_chunks = retrieve_relevant_chunks(
        query,
        chunks,
        chunk_embeddings,
        TOP_K
    )

    print("\n" + "=" * 60)
    print("RETRIEVED CHUNKS")
    print("=" * 60)

    for rank, item in enumerate(retrieved_chunks, start=1):

        print(f"\nRank #{rank}")
        print(f"Score: {item['score']:.4f}")

        preview = item["chunk"][:300]

        print(f"Chunk Preview:\n{preview}")

    # ---------------------------------------------------
    # STEP 6: GENERATE FINAL ANSWER
    # ---------------------------------------------------

    print("\n" + "=" * 60)
    print("GENERATING ANSWER")
    print("=" * 60)

    answer = generate_rag_answer(
        query,
        retrieved_chunks
    )

    print("\nFINAL ANSWER:\n")

    print(answer)

# ---------------------------------------------------
# RUN
# ---------------------------------------------------

if __name__ == "__main__":
    main()