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
def calculator(a: float, b: float, op: str) -> float:
    """Do arithmetic. op must be add, sub, mul or div."""

    operations = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b != 0 else float("nan"),
    }

    return operations[op]


@tool
def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())


@tool
def lookup_note(topic: str) -> str:
    """Look up study notes."""

    notes = {
        "python": "Python is a high-level language. Indentation defines blocks.",
        "groq": "Groq provides very fast inference for open-source LLMs.",
        "rag": "RAG retrieves documents before generating an answer.",
        "agent": "An agent follows the ReAct loop: Reason → Act → Observe.",
    }

    return notes.get(topic.lower(), "No note found.")


TOOLS = [
    calculator,
    word_count,
    lookup_note,
]

# ---------------------------------------------------------------------
# System Prompt
# ---------------------------------------------------------------------

SYSTEM_PROMPT = """
You are StudyBot.

Rules:

- Always use tools for calculations.
- Always use lookup_note for study topics.
- Always use word_count when counting words.
- Never guess tool results.
- Answer in one short paragraph.
"""

# ---------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------

model = ChatGroq(
    model=MODEL,
    temperature=0,
)

# ---------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------

agent = create_agent(
    model=model,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT,
)

print("=" * 60)
print("StudyBot")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    final_answer = ""

    print("\n=========== ReAct Loop ===========\n")

    for chunk in agent.stream(
        {
            "messages": [
                ("human", question)
            ]
        },
        stream_mode="updates",
    ):

        for node, update in chunk.items():

            last = update["messages"][-1]

            if getattr(last, "tool_calls", None):

                for call in last.tool_calls:

                    print(f"[{node}] TOOL CALL")
                    print(f"Tool : {call['name']}")
                    print(f"Args : {call['args']}")
                    print()

            elif last.__class__.__name__ == "ToolMessage":

                print(f"[{node}] TOOL RESULT")
                print(last.content)
                print()

            elif last.content:

                final_answer = last.content

                print(f"[{node}] ANSWER")
                print(last.content)
                print()

    print("-" * 60)
    print("StudyBot:", final_answer)
    print("-" * 60)