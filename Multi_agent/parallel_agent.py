import operator
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
)

class State(TypedDict):
    draft: str
    reviews: Annotated[list[str], operator.add]
    summary: str

def ask(system: str, user: str) -> str:
    try:
        response = llm.invoke([
            SystemMessage(content=system),
            HumanMessage(content=user)
        ])
        return response.content.strip()
    except Exception as e:
        print("LLM Error:", e)
        return "No response."

def review(name: str, system: str):
    def run(state: State):
        print(f"{name} reviewing...")
        note = ask(system, state["draft"])
        return {"reviews": [f"{name}: {note}"]}
    return run

fact_checker = review(
    "Fact Checker",
    "You are a fact checker. Point out any claims that need verification in 1-2 sentences."
)
seo_expert = review(
    "SEO Expert",
    "You are an SEO expert. Suggest one keyword or headline improvement in 1-2 sentences."
)
tone_expert = review(
    "Tone Expert",
    "You are a tone editor. Comment on whether the tone is suitable for a general audience in 1-2 sentences."
)

def aggregate(state: State):
    print("Aggregating reviews...")
    summary = "\n".join(f"- {item}" for item in state["reviews"])
    return {"summary": summary}

def build_graph():
    graph = StateGraph(State)

    graph.add_node("fact_checker", fact_checker)
    graph.add_node("seo_expert", seo_expert)
    graph.add_node("tone_expert", tone_expert)
    graph.add_node("aggregate", aggregate)
    graph.add_edge(START, "fact_checker")
    graph.add_edge(START, "seo_expert")
    graph.add_edge(START, "tone_expert")
    graph.add_edge("fact_checker", "aggregate")
    graph.add_edge("seo_expert", "aggregate")
    graph.add_edge("tone_expert", "aggregate")
    graph.add_edge("aggregate", END)
    return graph.compile()

def main():

    draft = input("\nEnter a draft:\n\n").strip()
    if not draft:
        print("Draft cannot be empty.")
        return

    panel = build_graph()
    result = panel.invoke({
        "draft": draft,
        "reviews": [],
        "summary": ""
    })

    print(result["summary"])

if __name__ == "__main__":
    main()