from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message: str
    category: str
    reply: str

def classify(state: State):
    text = state["message"].lower()
    if any(word in text for word in ["refund", "invoice", "payment", "charge"]):
        category = "billing"
    elif any(word in text for word in ["error", "bug", "login", "crash", "broken"]):
        category = "technical"
    else:
        category = "general"
    print(f"\n[Classifier] Category = {category}")
    return {"category": category}


def router(state: State):
    return state["category"]


def billing(state: State):
    return {
        "reply": (
            "Billing Team:\n"
            "We'll review your payment/refund request within 24 hours."
        )
    }


def technical(state: State):
    return {
        "reply": (
            "Technical Support:\n"
            "Please share your app version and a screenshot of the error."
        )
    }


def general(state: State):
    return {
        "reply": (
            "Customer Support:\n"
            "Thanks for contacting us. We'll get back to you shortly."
        )
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


print("Support Desk Bot")
print("Type 'exit' or 'quit' to stop.")

while True:
    user_input = input("\nYou the issue..... : ")

    if user_input.lower() in ["exit", "quit"]:
        print("\nGoodbye!")
        break

    initial_state = {
        "message": user_input,
        "category": "",
        "reply": "",
    }

    result = graph.invoke(initial_state)

    print(f"Category : {result['category']}")
    print(f"Bot      : {result['reply']}")