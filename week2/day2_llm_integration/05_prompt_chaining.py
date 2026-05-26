import requests
import json
import time

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "qwen2.5:7b"

INPUT_TEXT = """
Python is widely used in artificial intelligence,
machine learning, backend development,
automation, and data science.
Companies use Python because it is simple,
powerful, and has a massive ecosystem.
"""

# -----------------------------------
# HELPER FUNCTION
# -----------------------------------

def call_llm(prompt, retries=3):

    for attempt in range(retries):

        try:

            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            output = data.get("response", "").strip()

            if not output:
                raise ValueError("Empty model response.")

            return output

        except Exception as e:

            print(f"\nAttempt {attempt + 1} failed: {e}")

            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise

# -----------------------------------
# STEP 1 — EXTRACT
# -----------------------------------

extract_prompt = f"""
Extract the main topics from this text.

Return ONLY a comma-separated list.

Text:
{INPUT_TEXT}
"""

topics = call_llm(extract_prompt)

print("\n===== STEP 1: EXTRACTED TOPICS =====\n")
print(topics)

# -----------------------------------
# STEP 2 — TRANSFORM
# -----------------------------------

transform_prompt = f"""
Convert these topics into short bullet-point study notes.

Topics:
{topics}
"""

notes = call_llm(transform_prompt)

print("\n===== STEP 2: TRANSFORMED NOTES =====\n")
print(notes)

# -----------------------------------
# STEP 3 — SUMMARIZE
# -----------------------------------

summary_prompt = f"""
Summarize these study notes in 3 concise sentences.

Notes:
{notes}
"""

summary = call_llm(summary_prompt)

print("\n===== STEP 3: FINAL SUMMARY =====\n")
print(summary)