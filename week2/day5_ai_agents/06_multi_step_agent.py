from pathlib import Path
from langchain_ollama import ChatOllama

# ---------------------
# MODEL
# ---------------------

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

# ---------------------
# STEP 1
# READ FILE
# ---------------------

input_file = Path("sample_report.txt")

content = input_file.read_text(
    encoding="utf-8"
)

print("\nSTEP 1 COMPLETE")
print("File Read Successfully")

# ---------------------
# STEP 2
# SUMMARIZE
# ---------------------

prompt = f"""
Summarize the following text
in 3 sentences:

{content}
"""

summary = llm.invoke(
    prompt
).content

print("\nSTEP 2 COMPLETE")
print(summary)

# ---------------------
# STEP 3
# SAVE
# ---------------------

output_file = Path(
    "summary_report.txt"
)

output_file.write_text(
    summary,
    encoding="utf-8"
)

print("\nSTEP 3 COMPLETE")
print("Summary Saved")

# ---------------------
# STEP 4
# VERIFY
# ---------------------

if output_file.exists():

    print("\nSTEP 4 COMPLETE")
    print("Verification Passed")

else:

    print("Verification Failed")