import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()

MODEL = "llama-3.1-8b-instant"

# -------------------- Tools --------------------

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        return "Error: Division by zero."
    return a / b


@tool
def power(a: float, b: float) -> float:
    """Raise the first number to the power of the second."""
    return a ** b


@tool
def modulus(a: int, b: int) -> int:
    """Return remainder after division."""
    return a % b


TOOLS = [add, subtract, multiply, divide, power, modulus]
TOOL_MAP = {tool.name: tool for tool in TOOLS}

# -------------------- Tool Calling Loop --------------------

def run_loop(model, question):
    messages = [HumanMessage(content=question)]

    while True:
        ai = model.invoke(messages)
        messages.append(ai)

        # Final answer
        if not ai.tool_calls:
            return ai.content

        # Execute requested tools
        for call in ai.tool_calls:
            tool_name = call["name"]
            args = call["args"]

            result = TOOL_MAP[tool_name].invoke(args)

            print(f"Tool Called: {tool_name}")
            print(f"Arguments : {args}")
            print(f"Result    : {result}\n")

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=call["id"],
                )
            )

# -------------------- Model --------------------

from langchain_groq import ChatGroq

model = ChatGroq(
    model=MODEL,
    temperature=0
).bind_tools(TOOLS)

# -------------------- Calculator --------------------

print("=== AI Calculator ===")
print("Type 'exit' to quit.\n")

while True:
    question = input("Enter calculation: ")

    if question.lower() == "exit":
        break

    answer = run_loop(model, question)
    print("Answer:", answer)
    print("-" * 40)