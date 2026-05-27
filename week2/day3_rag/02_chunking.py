from pathlib import Path
import fitz
import nltk

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR / "data" / "sample.pdf"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ---------------------------------------------------
# EXTRACT TEXT
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
# FIXED-SIZE CHUNKING
# ---------------------------------------------------

def fixed_chunking(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


# ---------------------------------------------------
# FIXED-SIZE CHUNKING WITH OVERLAP
# ---------------------------------------------------

def chunk_with_overlap(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# ---------------------------------------------------
# SENTENCE-AWARE CHUNKING
# ---------------------------------------------------

def sentence_chunking(text, chunk_size=500):

    sentences = nltk.sent_tokenize(text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:

        # If adding sentence exceeds chunk size,
        # save current chunk and start new one
        if len(current_chunk) + len(sentence) > chunk_size:

            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

        else:
            current_chunk += sentence + " "

    # Add remaining chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

def main():

    print("=" * 60)
    print("CHUNKING DEMO")
    print("=" * 60)

    text = extract_text_from_pdf(PDF_PATH)

    if not text:
        print("[ERROR] No text extracted")
        return

    print(f"\nTotal text length: {len(text)} characters")

    # ---------------------------------------------------
    # FIXED CHUNKING
    # ---------------------------------------------------

    fixed_chunks = fixed_chunking(text, CHUNK_SIZE)

    print("\n" + "=" * 60)
    print("FIXED CHUNKING")
    print("=" * 60)

    print(f"Number of chunks: {len(fixed_chunks)}")

    print("\nFirst chunk preview:\n")
    print(fixed_chunks[0][:500])

    # ---------------------------------------------------
    # OVERLAP CHUNKING
    # ---------------------------------------------------

    overlap_chunks = chunk_with_overlap(
        text,
        CHUNK_SIZE,
        CHUNK_OVERLAP
    )

    print("\n" + "=" * 60)
    print("CHUNKING WITH OVERLAP")
    print("=" * 60)

    print(f"Number of chunks: {len(overlap_chunks)}")

    print("\nFirst chunk preview:\n")
    print(overlap_chunks[0][:500])

    # ---------------------------------------------------
    # SENTENCE CHUNKING
    # ---------------------------------------------------

    sentence_chunks = sentence_chunking(text, CHUNK_SIZE)

    print("\n" + "=" * 60)
    print("SENTENCE-AWARE CHUNKING")
    print("=" * 60)

    print(f"Number of chunks: {len(sentence_chunks)}")

    print("\nFirst chunk preview:\n")
    print(sentence_chunks[0][:500])


if __name__ == "__main__":
    main()