from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq

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

print("=" * 60)
print(f"Using Groq Model: {MODEL}")
print("Type 'exit' to quit.")
print("=" * 60)

# ---------------------------------------------------------------------
# Chat Loop
# ---------------------------------------------------------------------

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    print("\n========== ReAct Loop ==========\n")

    final_answer = ""

    for chunk in agent.stream(
        {"messages": [("human", question)]},
        stream_mode="updates",
    ):

        for node, update in chunk.items():

            last = update["messages"][-1]

            # ---------------- Tool Call ----------------
            if getattr(last, "tool_calls", None):

                for call in last.tool_calls:
                    print(f"[{node}] REASON + ACT")
                    print(f"   Tool : {call['name']}")
                    print(f"   Args : {call['args']}")
                    print()

            # ---------------- Tool Result ----------------
            elif last.__class__.__name__ == "ToolMessage":

                print(f"[{node}] OBSERVE")
                print(f"   Result : {last.content}")
                print()

            # ---------------- Final Answer ----------------
            elif last.content:

                final_answer = last.content

                print(f"[{node}] ANSWER")
                print(f"   {last.content}")
                print()

    print("-" * 60)
    print("Final Answer:")
    print(final_answer)
    print("-" * 60)