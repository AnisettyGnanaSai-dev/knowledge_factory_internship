# Context Windows

## What is a Context Window?
The maximum number of tokens an LLM can process simultaneously.

## Important Realization
LLMs do not truly remember.
Conversation history is repeatedly re-sent as context.

## What Consumes Context?
- System prompts
- User prompts
- Assistant replies
- Retrieved documents
- Generated outputs

## Problems
- Truncation
- Lost in the middle
- Attention dilution
- Cost increase

## Why RAG Exists
RAG retrieves only relevant information instead of sending everything into context.

## My Understanding
(write in your own words)