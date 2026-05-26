import requests
import json
import time

OLLAMA_URL = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:7b",
    "prompt":
    """You are a senior Python mentor.

Explain what a REST API is in simple terms.
Give:
1. Simple explanation
2. Real-world example
3. One analogy
""",
"stream": False
}
start_time = time.time()

try:
    response = requests.post(OLLAMA_URL,json = payload, timeout=10000)
    response.raise_for_status()

    data = response.json()

    generated_text = data.get("responses", "").strip()

    if not generated_text:
        raise ValueError("Empty response")
    
    end_time = time.time()

    print(generated_text)
    print(f"Model used : {data.get('model')}")
    print(f"Time Taken: {end_time - start_time:.2f} sec")
except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to Ollama.")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except json.JSONDecodeError:
    print("Invalid JSON response.")

except ValueError as e:
    print(f"Validation Error: {e}")

except Exception as e:
    print(f"Unexpected Error: {e}")
