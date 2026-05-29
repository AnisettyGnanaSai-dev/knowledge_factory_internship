# 01_langchain_basics.py

# Prompt handling
from langchain_core.prompts import PromptTemplate

# Ollama model wrapper
from langchain_ollama import ChatOllama

# Output parser
from langchain_core.output_parsers import StrOutputParser

# Local qwen model
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

# Dynamic prompt
prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
You are a helpful AI assistant.

Summarize the topic below in 100 words.

Topic:
{topic}
"""
)

# Convert model response to plain text
parser = StrOutputParser()

# LCEL chain
chain = prompt | llm | parser

# Run chain
result = chain.invoke({
    "topic": "Artificial Intelligence"
})

print("\nSUMMARY:\n")
print(result)