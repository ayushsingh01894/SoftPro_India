from typing import List, Tuple

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

MODEL = "llama-3.3-70b-versatile"

# ---------------------------------------------------------------------
# TOOLS
# ---------------------------------------------------------------------

@tool
def calculator(a: float, b: float, op: str) -> float:
    """Perform arithmetic. op = add, sub, mul, div"""

    operations = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b if b else float("nan"),
    }

    return operations[op]


@tool
def search_handbook(topic: str) -> str:
    """Search Softpro handbook."""

    topic = topic.lower().strip()

    if "fee" in topic:
        return "Semester fee is Rs.2500, due by the 10th."

    elif "hostel" in topic:
        return "Hostel fee is Rs.1200/month including WiFi."

    elif "library" in topic:
        return "Library opens from 9AM to 9PM."

    elif "exam" in topic:
        return "75% attendance is required for exams."

    elif "wifi" in topic:
        return "Connect to Softpro-Net using your Roll Number."

    return handbook.get(
        topic.lower(),
        "No handbook entry found."
    )


@tool
def word_count(text: str) -> int:
    """Count words."""
    return len(text.split())


TOOLS = [
    calculator,
    search_handbook,
    word_count,
]

# ---------------------------------------------------------------------
# SYSTEM PROMPT
# ---------------------------------------------------------------------

SYSTEM_PROMPT = """
You are SoftBot.

Rules:

- Always use calculator for maths.
- Always use search_handbook for fees, hostel, exam, wifi or library questions.
- Always use word_count when asked to count words.
- Never guess.
- Answer politely in one or two short sentences.
"""

# ---------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------

model = ChatGroq(
    model=MODEL,
    temperature=0,
)

# ---------------------------------------------------------------------
# AGENT
# ---------------------------------------------------------------------

agent = create_agent(
    model=model,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT,
    checkpointer=MemorySaver(),
)

# ---------------------------------------------------------------------
# MEMORY CONFIG
# ---------------------------------------------------------------------

config = {
    "configurable": {
        "thread_id": "student-1"
    }
}

# ---------------------------------------------------------------------
# RUN TURN
# ---------------------------------------------------------------------

def run_turn(question: str):

    trace = []
    answer = ""

    for chunk in agent.stream(
        {
            "messages": [
                ("human", question)
            ]
        },
        config=config,
        stream_mode="updates",
    ):

        for node, update in chunk.items():

            last = update["messages"][-1]

            if getattr(last, "tool_calls", None):

                for call in last.tool_calls:
                    trace.append(
                        f"Called {call['name']} {call['args']}"
                    )

            elif last.__class__.__name__ == "ToolMessage":

                trace.append(
                    f"Result : {last.content}"
                )

            elif last.content:

                answer = last.content

    return answer, trace

# ---------------------------------------------------------------------
# CHAT LOOP
# ---------------------------------------------------------------------

print("=" * 60)
print("SoftBot")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    answer, trace = run_turn(question)

    print("\nSoftBot:", answer)

    if trace:

        print("\nHow I got this:")

        for step in trace:
            print("-", step)