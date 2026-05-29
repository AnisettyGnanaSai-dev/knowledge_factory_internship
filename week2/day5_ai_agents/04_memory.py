from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

chat_history = []

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(
        f"User: {user_input}"
    )

    prompt = "\n".join(chat_history)

    response = llm.invoke(prompt)

    answer = response.content

    print("\nAI:", answer)

    chat_history.append(
        f"AI: {answer}"
    )