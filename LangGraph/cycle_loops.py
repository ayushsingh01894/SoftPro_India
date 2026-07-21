"""
START
   |
generate_email
      |
      v
review_email
      |
   review()
   /      \
retry     done
  |         |
  └─────────┘
      |
     END

"""

from typing import TypedDict
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


class State(TypedDict):
    topic: str
    email: str
    feedback: str
    attempts: int


def generate_email(state: State):
    prompt = f"""
Write a professional email.

Request:
{state["topic"]}

Previous Feedback:
{state["feedback"]}

If feedback is empty, write the first draft.
Otherwise improve the email according to the feedback.
"""

    email = llm.invoke(prompt).content

    print(f"\nAttempt {state['attempts'] + 1}")
    print("-" * 50)
    print(email)

    return {
        "email": email,
        "attempts": state["attempts"] + 1
    }


def review_email(state: State):
    prompt = f"""
Review this email.

Rules:
- Professional
- Clear
- Complete
- Grammatically correct

If the email is good, reply only:

PASS

Otherwise reply exactly like:

RETRY: <one short improvement>

Email:
{state["email"]}
"""

    review = llm.invoke(prompt).content.strip()

    print("\nReview:")
    print(review)

    return {
        "feedback": review
    }


MAX_ATTEMPTS = 3


def router(state: State):
    feedback = state["feedback"].upper()

    if feedback.startswith("PASS"):
        return "done"

    if state["attempts"] >= MAX_ATTEMPTS:
        return "done"

    return "retry"


builder = StateGraph(State)

builder.add_node("generate", generate_email)
builder.add_node("review", review_email)

builder.add_edge(START, "generate")
builder.add_edge("generate", "review")

builder.add_conditional_edges(
    "review",
    router,
    {
        "retry": "generate",
        "done": END,
    },
)

graph = builder.compile()


print("AI Email Writer")
print("Type 'exit' to quit.\n")

while True:

    topic = input("Email Request: ")

    if topic.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = graph.invoke(
        {
            "topic": topic,
            "email": "",
            "feedback": "",
            "attempts": 0,
        }
    )

    print("\n" + "=" * 60)
    print("Final Email\n")
    print(result["email"])
    print("=" * 60)