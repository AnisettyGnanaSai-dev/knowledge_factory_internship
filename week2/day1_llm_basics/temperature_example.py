from openai import OpenAI

# 1. Point the client to your local Ollama instance
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Ollama ignores this, but the OpenAI library requires a placeholder string
)

# 2. Call your local Qwen 2.5 7B model instead of gpt-4
response = client.chat.completions.create(
    model="qwen2.5:7b",  
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short creative poem about a clever fox."}
    ],
    temperature=0.1  # Your temperature logic remains exactly the same!
)

print(response.choices[0].message.content)