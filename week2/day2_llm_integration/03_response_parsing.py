import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

prompt = """
Return ONLY valid JSON.

Format:
{
  "summary": "...",
  "sentiment": "...",
  "keywords": ["...", "..."]
}

Text:
Python is a powerful programming language used in AI.
"""

payload = {
    "model": "qwen2.5:7b",
    "prompt": prompt,
    "stream": False
}

try:
    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=10000
    )

    response.raise_for_status()

    data = response.json()

    raw_output = data.get("response", "").strip()

    print("\n===== RAW MODEL OUTPUT =====\n")
    print(raw_output)

    parsed_json = json.loads(raw_output)

    print("\n===== PARSED JSON =====\n")
    print(json.dumps(parsed_json, indent=4))

except json.JSONDecodeError:
    print("\nModel returned INVALID JSON.")

except Exception as e:
    print(f"Error: {e}")