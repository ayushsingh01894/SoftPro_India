import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq

# Load .env
load_dotenv()

MODEL = "llama-3.3-70b-versatile"

# ---------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------

@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the product."""
    return a * b


TOOLS = [add, multiply]

# ---------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------

model = ChatGroq(
    model=MODEL,
    temperature=0
)

# ---------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------

agent = create_agent(
    model=model,
    tools=TOOLS,
)

# ---------------------------------------------------------------------
# Chat Loop
# ---------------------------------------------------------------------

print("=" * 60)
print("ReAct Agent")
print("Type 'exit' to quit.")
print("=" * 60)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = agent.invoke(
        {
            "messages": [
                ("human", user_input)
            ]
        }
    )

    print("\nAgent:", result["messages"][-1].content)