from typing import TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


class State(TypedDict):
    message: str
    category: str
    reply: str


def classify(state: State):
    prompt = f"""
        Classify the following customer support message into exactly one category.
        Categories:
            - billing
            - technical
            - general
        Reply with only the category name.
        Message:
            {state["message"]}
        """
    category = llm.invoke(prompt).content.strip().lower()
    if category not in ["billing", "technical", "general"]:
        category = "general"
    print(f"\nCategory Selected: {category}")
    return {"category": category}


def router(state: State):
    return state["category"]


def billing(state: State):
    return {
        "reply": "Billing Team: We'll review your payment or refund request within 24 hours."
    }


def technical(state: State):
    return {
        "reply": "Technical Support: Please share your app version and a screenshot of the issue."
    }


def general(state: State):
    return {
        "reply": "Customer Support: Thank you for contacting us. We'll get back to you shortly."
    }


builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("billing", billing)
builder.add_node("technical", technical)
builder.add_node("general", general)
builder.add_edge(START, "classify")
builder.add_conditional_edges(
    "classify",
    router,
    {
        "billing": "billing",
        "technical": "technical",
        "general": "general",
    },
)

builder.add_edge("billing", END)
builder.add_edge("technical", END)
builder.add_edge("general", END)

graph = builder.compile()

print("AI Support Desk")
print("Type 'exit' to quit.")

while True:
    user = input("\nYou: ")

    if user.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = graph.invoke(
        {
            "message": user,
            "category": "",
            "reply": "",
        }
    )

    print(f"Category : {result['category']}")
    print(f"Bot      : {result['reply']}")