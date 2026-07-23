from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

MODEL = "llama-3.3-70b-versatile"

# ---------------------------------------------------------------------
# Tool
# ---------------------------------------------------------------------

@tool
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


# ---------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------

model = ChatGroq(
    model=MODEL,
    temperature=0,
)

# ---------------------------------------------------------------------
# Agent + Memory
# ---------------------------------------------------------------------

memory = MemorySaver()

agent = create_agent(
    model=model,
    tools=[add],
    checkpointer=memory,
)

print("=" * 60)
print("Agent with Memory")
print("Type 'exit' to quit.")
print("=" * 60)

# ---------------------------------------------------------------------
# Thread ID
# ---------------------------------------------------------------------

thread_id = input("Enter Thread ID (example: student-1): ").strip()

if not thread_id:
    thread_id = "student-1"

config = {
    "configurable": {
        "thread_id": thread_id
    }
}

print(f"\nConversation started with thread: {thread_id}")

# ---------------------------------------------------------------------
# Chat Loop
# ---------------------------------------------------------------------

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = agent.invoke(
        {
            "messages": [
                ("human", question)
            ]
        },
        config=config,
    )

    print("\nAgent:", result["messages"][-1].content)

    # Show how many messages are stored
    state = agent.get_state(config)

    if state and "messages" in state.values:
        print(f"\nMemory contains {len(state.values['messages'])} messages.")