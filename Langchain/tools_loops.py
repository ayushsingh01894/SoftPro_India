import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()

MODEL = "llama-3.1-8b-instant"

# Define Tools

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def word_count(text: str) -> int:
    """Count how many words are in a text."""
    return len(text.split())


TOOLS = [multiply, word_count]
TOOL_MAP = {tool.name: tool for tool in TOOLS}


# Agent Loop

def run_loop(model, question):
    """
    Runs the model until it stops requesting tools.
    """
    messages = [HumanMessage(content=question)]

    while True:

        # Ask the model
        ai = model.invoke(messages)
        messages.append(ai)

        # If no tool calls, return final answer
        if not ai.tool_calls:
            return ai.content

        # Execute each requested tool
        for call in ai.tool_calls:

            tool_name = call["name"]
            tool_args = call["args"]

            print(f"\n🔧 Calling Tool: {tool_name}")
            print(f"Arguments: {tool_args}")
            result = TOOL_MAP[tool_name].invoke(tool_args)
            print(f"Tool Result: {result}")

            # Send tool result back to model
            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=call["id"],
                )
            )


# Main

def main():

    # Check API Key
    if not os.getenv("GROQ_API_KEY"):
        print("❌ GROQ_API_KEY not found.")
        return

    from langchain_groq import ChatGroq

    model = ChatGroq(
        model=MODEL,
        temperature=0,
    ).bind_tools(TOOLS)

    while True:

        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() in ["exit", "quit"]:
            break

        answer = run_loop(model, question)
        print("\n==============================")
        print("Final Answer:")
        print(answer)
        print("==============================")


if __name__ == "__main__":
    main()