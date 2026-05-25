import requests

# updated by codex: switched to package-safe imports
from api_time_machine.config.settings import (
    OLLAMA_URL,
    OLLAMA_MODEL
)

# updated by codex: switched to package-safe imports
from api_time_machine.utils.prompt_builder import build_analysis_prompt


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
