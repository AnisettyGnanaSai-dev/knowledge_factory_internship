from langchain_ollama import ChatOllama
from langchain_core.tools import tool

# -------------------------
# TOOL 1
# -------------------------

@tool
def calculator_tool(expression: str) -> str:
    """
    Evaluate mathematical expressions.
    Example: 50*10
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

# -------------------------
# TOOL 2
# -------------------------

@tool
def word_count_tool(text: str) -> str:
    """
    Count words in text.
    """
    return str(len(text.split()))

# -------------------------
# TOOL 3
# -------------------------

@tool
def file_reader_tool(filepath: str) -> str:
    """
    Read a text file.
    """
    try:
        with open(filepath,"r",encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return str(e)

# -------------------------
# MODEL
# -------------------------

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

tools = [
    calculator_tool,
    word_count_tool,
    file_reader_tool
]

print("Tools Loaded:")
for tool in tools:
    print("-", tool.name)