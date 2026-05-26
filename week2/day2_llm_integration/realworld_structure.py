from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("OLLAMA_BASE_URL")
print(f"Ollama Base URL: {base_url}")