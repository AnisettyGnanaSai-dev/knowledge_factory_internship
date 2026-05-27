import ollama

# ---------------------------------------------------
# FAKE COMPANY DOCUMENT
# ---------------------------------------------------

company_policy = """
Travel Reimbursement Policy

Employees may claim up to ₹18,000 per quarter
for business travel expenses.

Claims above this amount require manager approval.
"""

# ---------------------------------------------------
# USER QUESTION
# ---------------------------------------------------

question = "What is the travel reimbursement limit?"

# ---------------------------------------------------
# 1. NORMAL LLM (NO RAG)
# ---------------------------------------------------

print("\n" + "=" * 60)
print("WITHOUT RAG")
print("=" * 60)

try:
    response_no_rag = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print(response_no_rag["message"]["content"])

except Exception as e:
    print(f"Error calling Ollama: {e}")

# ---------------------------------------------------
# 2. RAG PROMPT
# ---------------------------------------------------

print("\n" + "=" * 60)
print("WITH RAG")
print("=" * 60)

rag_prompt = f"""
Answer the question based ONLY on the context below.

If the answer is not in the context, say "I don't know."

Context:
{company_policy}

Question:
{question}
"""

try:
    response_rag = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": rag_prompt
            }
        ]
    )

    print(response_rag["message"]["content"])

except Exception as e:
    print(f"Error calling Ollama: {e}")