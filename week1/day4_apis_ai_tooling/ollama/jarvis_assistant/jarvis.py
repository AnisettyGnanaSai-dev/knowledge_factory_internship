import os
import requests

from voice.speech_to_text import listen
from voice.text_to_speech import speak

# ==============================
# OLLAMA API URL
# ==============================

OLLAMA_URL = "http://localhost:11434/api/chat"

# ==============================
# GET CURRENT DIRECTORY
# ==============================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# ==============================
# SYSTEM PROMPT FILE PATH
# ==============================

PROMPT_PATH = os.path.join(
    BASE_DIR,
    "system_prompt.txt"
)

# ==============================
# LOAD SYSTEM PROMPT
# ==============================

with open(
    PROMPT_PATH,
    "r",
    encoding="utf-8"
) as file:

    system_prompt = file.read()

# ==============================
# CONVERSATION MEMORY
# ==============================

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

# ==============================
# STARTUP MESSAGE
# ==============================

speak(
    "Good evening, sir. JARVIS systems are now online."
)

# ==============================
# MAIN LOOP
# ==============================

while True:

    # LISTEN TO USER
    user_input = listen()

    # IF NOTHING HEARD
    if not user_input:

        speak(
            "I'm afraid I didn't catch that, sir."
        )

        continue

    # PRINT USER INPUT
    print(f"\nYou: {user_input}")

    # ==============================
    # EXIT COMMANDS
    # ==============================

    if user_input.lower() in [
        "exit",
        "quit",
        "shutdown",
        "goodbye"
    ]:

        speak(
            "Very good, sir. Shutting down systems."
        )

        break

    # ==============================
    # SAVE USER MESSAGE
    # ==============================

    messages.append({
        "role": "user",
        "content": user_input
    })

    # ==============================
    # REQUEST PAYLOAD
    # ==============================

    payload = {
        "model": "qwen2.5:3b",
        "messages": messages,
        "stream": False
    }

    try:

        # ==============================
        # SEND REQUEST TO OLLAMA
        # ==============================

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        # CHECK STATUS
        print(
            f"\nStatus Code: {response.status_code}"
        )

        # CONVERT RESPONSE
        data = response.json()

        # EXTRACT AI RESPONSE
        assistant_reply = data[
            "message"
        ]["content"]

        # PRINT RESPONSE
        print(
            f"\nJARVIS: {assistant_reply}\n"
        )

        # SPEAK RESPONSE
        speak(assistant_reply)

        # SAVE RESPONSE TO MEMORY
        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

    except Exception as e:

        print("\nERROR OCCURRED:")
        print(e)

        speak(
            "I'm afraid an error has occurred, sir."
        )