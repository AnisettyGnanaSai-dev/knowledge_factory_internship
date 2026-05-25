import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:3b",
    "prompt": "Explain the concept of machine learning in simple terms.",
    "stream": False
}

response = requests.post(url, json=payload)
data = response.json()
print("Status:", response.status_code)
print("Response:", data["response"])