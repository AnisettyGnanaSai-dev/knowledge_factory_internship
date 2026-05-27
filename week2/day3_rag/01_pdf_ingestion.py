import fitz  # PyMuPDF
import pdfplumber
from pathlib import Path

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

PDF_PATH = BASE_DIR / "data" / "sample.pdf"

# ---------------------------------------------------
# FUNCTION: Extract text using PyMuPDF
# ---------------------------------------------------

def extract_with_pymupdf(pdf_path):
    """
    Fast PDF text extraction using PyMuPDF.
    Best default choice for most RAG systems.
    """

    full_text = []

    try:
        doc = fitz.open(pdf_path)

        print(f"\nOpened PDF with {len(doc)} pages")

        for page_number, page in enumerate(doc, start=1):

            text = page.get_text()

            # Basic cleaning
            text = text.strip()

            if text:
                full_text.append({
                    "page": page_number,
                    "text": text
                })
            else:
                print(f"[WARNING] No text found on page {page_number}")

        doc.close()

        return full_text

    except Exception as e:
        print(f"[ERROR] PyMuPDF extraction failed: {e}")
        return []


# ---------------------------------------------------
# FUNCTION: Extract tables using pdfplumber
# ---------------------------------------------------

def extract_tables(pdf_path):
    """
    Extract tables separately using pdfplumber.
    Useful for financial statements and reports.
    """

    tables = []

    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                extracted_tables = page.extract_tables()

                if extracted_tables:

                    for table in extracted_tables:
                        tables.append({
                            "page": page_number,
                            "table": table
                        })

        return tables

    except Exception as e:
        print(f"[ERROR] Table extraction failed: {e}")
        return []


# ---------------------------------------------------
# FUNCTION: Detect possible scanned PDFs
# ---------------------------------------------------

def detect_scanned_pdf(extracted_pages):
    """
    Heuristic:
    If most pages have almost no text,
    the PDF may be scanned/image-only.
    """

    empty_pages = 0

    for page in extracted_pages:

        if len(page["text"]) < 30:
            empty_pages += 1

    total_pages = len(extracted_pages)

    if total_pages == 0:
        return True

    empty_ratio = empty_pages / total_pages

    return empty_ratio > 0.7


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

def main():

    # Check file exists
    if not Path(PDF_PATH).exists():
        print(f"[ERROR] PDF not found: {PDF_PATH}")
        return

    print("=" * 60)
    print("PDF INGESTION DEMO")
    print("=" * 60)

    # ---------------------------------------------------
    # TEXT EXTRACTION
    # ---------------------------------------------------

    pages = extract_with_pymupdf(PDF_PATH)

    print(f"\nExtracted text from {len(pages)} pages")

    # Show preview
    for page in pages[:2]:

        print("\n" + "-" * 60)
        print(f"PAGE: {page['page']}")
        print("-" * 60)

        preview = page["text"][:500]

        print(preview)

    # ---------------------------------------------------
    # DETECT SCANNED PDF
    # ---------------------------------------------------

    is_scanned = detect_scanned_pdf(pages)

    print("\n" + "=" * 60)

    if is_scanned:
        print("[WARNING] PDF may be scanned/image-only")
        print("OCR may be required")
    else:
        print("[OK] PDF appears to contain real text")

    # ---------------------------------------------------
    # TABLE EXTRACTION
    # ---------------------------------------------------

    tables = extract_tables(PDF_PATH)

    print("\n" + "=" * 60)
    print(f"Found {len(tables)} tables")

    if tables:

        first_table = tables[0]

        print("\nFirst table preview:")
        print(first_table["table"][:5])


if __name__ == "__main__":
    main()