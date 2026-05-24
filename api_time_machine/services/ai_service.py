import requests

from config.settings import (
    OLLAMA_URL,
    OLLAMA_MODEL
)

from utils.prompt_builder import build_analysis_prompt


class AIService:

    @staticmethod
    def analyze_request(request_data):

        prompt = build_analysis_prompt(request_data)

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        return result.get("response")