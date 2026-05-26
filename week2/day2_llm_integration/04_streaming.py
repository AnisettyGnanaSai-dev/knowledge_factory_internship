import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:7b",
    "prompt": "Explain transformers in deep learning simply in 3 lines.",
    "stream": True
}

try:
    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True,
        timeout=120
    )

    response.raise_for_status()

    print("\n===== STREAMING RESPONSE =====\n")

    for line in response.iter_lines():

        if line:

            decoded_line = line.decode("utf-8")

            data = json.loads(decoded_line)

            token = data.get("response", "")

            print(token, end="", flush=True)

    print("\n")

except requests.exceptions.Timeout:
    print("Streaming request timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to Ollama.")

except json.JSONDecodeError:
    print("Invalid JSON during streaming.")

except Exception as e:
    print(f"Unexpected Error: {e}")