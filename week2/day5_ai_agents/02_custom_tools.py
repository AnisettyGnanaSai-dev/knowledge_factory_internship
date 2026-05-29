from langchain_core.tools import tool

@tool
def calculator_tool(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """

    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)


@tool
def word_count_tool(text: str) -> str:
    """
    Count words in text.
    """

    return str(len(text.split()))


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


print(calculator_tool.invoke("100+50"))
print(word_count_tool.invoke("Hello LangChain world"))
print(
    file_reader_tool.invoke(
        "week2/day5_ai_agents/sample.txt"
    )
)