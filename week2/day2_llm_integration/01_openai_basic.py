import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:7b",
    "prompt": "Explain the concept of recursion in programming in simple terms.",
    "stream": False
}

try :
    response = requests.post(OLLAMA_URL, json=payload, timeout=10000)  # Set a timeout for the request

    response.raise_for_status()  # Check if the request was successful

    data = response.json()

    print("Response from Ollama:")
    print(data["response"])

except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.")
except requests.exceptions.ConnectionError:
    print("Could not connect to the Ollama server. Please ensure it is running and accessible")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
              