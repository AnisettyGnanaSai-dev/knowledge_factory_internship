# 05_workflow_chain.py

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

parser = StrOutputParser()

outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
Create a research outline for:

{topic}
"""
)

summary_prompt = PromptTemplate(
    input_variables=["outline"],
    template="""
Write a summary from:

{outline}
"""
)

translation_prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
Translate into Telugu:

{summary}
"""
)

outline_chain = outline_prompt | llm | parser
summary_chain = summary_prompt | llm | parser
translation_chain = translation_prompt | llm | parser

topic = "AI Agents"

outline = outline_chain.invoke({
    "topic": topic
})

summary = summary_chain.invoke({
    "outline": outline
})

telugu = translation_chain.invoke({
    "summary": summary
})

print("\nOUTLINE:\n")
print(outline)

print("\nSUMMARY:\n")
print(summary)

print("\nTELUGU:\n")
print(telugu)