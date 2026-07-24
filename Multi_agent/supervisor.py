from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

WORKERS = ["billing", "tech", "general"]


class State(TypedDict):
    request: str
    next: str
    answer: str
    handled_by: str


def _ask(system: str, user: str) -> str:
    try:
        response = llm.invoke(
            [
                SystemMessage(content=system),
                HumanMessage(content=user),
            ]
        )
        return response.content.strip()
    except Exception as e:
        print("\nLLM ERROR:", e)
        return ""


def supervisor(state: State):
    if state.get("answer"):
        print("Worker completed task.")
        return {"next": "FINISH"}

    system = """
                You are a customer support supervisor.
                Choose ONLY ONE of these words:
                billing
                tech
                general
                Do not explain anything.
                Return only one word.
             """
    choice = _ask(system, state["request"]).lower()
    print("LLM Choice:", choice)

    if "billing" in choice:
        choice = "billing"
    elif "tech" in choice:
        choice = "tech"
    else:
        choice = "general"
    print("Routing ->", choice)
    return {"next": choice}


def worker(name: str, persona: str):
    def run(state: State):
        print(f"{name.upper()} WORKER")

        answer = _ask(persona, state["request"])
        print(answer)
        return {
            "answer": answer,
            "handled_by": name,
        }
    return run


billing = worker(
    "billing",
    "You are a billing support specialist. Answer briefly in 2-3 sentences.",
)
tech = worker(
    "tech",
    "You are a technical support specialist. Answer briefly in 2-3 sentences.",
)
general = worker(
    "general",
    "You are a friendly customer support agent. Answer briefly in 2-3 sentences.",
)


def route(state: State):
    print("\nRouter Decision:", state["next"])
    if state["next"] == "FINISH":
        return END
    return state["next"]


def build_graph():
    graph = StateGraph(State)
    graph.add_node("supervisor", supervisor)
    graph.add_node("billing", billing)
    graph.add_node("tech", tech)
    graph.add_node("general", general)
    graph.add_edge(START, "supervisor")
    graph.add_conditional_edges(
        "supervisor",
        route,
        {
            "billing": "billing",
            "tech": "tech",
            "general": "general",
            END: END,
        },
    )
    graph.add_edge("billing", "supervisor")
    graph.add_edge("tech", "supervisor")
    graph.add_edge("general", "supervisor")
    return graph.compile()

def main():

    desk = build_graph()

    while True:
        request = input(
            "\nEnter customer request (type 'exit' to quit): "
        ).strip()
        if request.lower() == "exit":
            break
        if not request:
            continue
        print("\nInvoking graph...\n")
        result = desk.invoke(
            {
                "request": request,
                "next": "",
                "answer": "",
                "handled_by": "",
            }
        )
        print(result["answer"])


if __name__ == "__main__":
    main()