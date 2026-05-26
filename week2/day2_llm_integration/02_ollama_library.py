from ollama import chat
from ollama import ChatResponse

try:
    response: ChatResponse = chat(
     model = 'qwen2.5:7b',
     messages = [
         {
             'role': 'system',
             'content': 'youre a helpful ai teacher.'
         },
         {
             'role': 'user',
             'content': 'Explain ollama in 3 lines'
         }
     ]   
    )

    answers = response.message.content

    print(answers)

except Exception as e:
    print(f"Exception:{e}")