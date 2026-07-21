import os
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

MODEL = "llama-3.1-8b-instant"

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found.")

from langchain_groq import ChatGroq

model = ChatGroq(
    model=MODEL,
    temperature=0
)


def chatbot(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(MessagesState)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)

thread_id = input("Enter Thread ID: ").strip()
config = {
    "configurable": {
        "thread_id": thread_id
    }
}

print("\nChat started.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = graph.invoke(
        {
            "messages": [("human", user_input)]
        },
        config=config
    )
    print("Bot:", result["messages"][-1].content)