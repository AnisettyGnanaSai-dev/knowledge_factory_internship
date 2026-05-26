from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

try:
    response = client.chat.completions.create(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI tutor."
            },
            {
                "role": "user",
                "content": "Explain Python decorators simply."
            }
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content

    print("\n===== RESPONSE =====\n")
    print(answer)

except Exception as e:
    print(f"Error: {e}")