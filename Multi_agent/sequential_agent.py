from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

class State(TypedDict):
    topic: str
    research: str
    draft: str
    final: str 


def _ask(role_system: str, user: str) -> str:
    reply = llm.invoke([SystemMessage(content=role_system), HumanMessage(content=user)])
    return reply.content.strip()

def researcher(state: State) -> dict:
    system = (
        "You are a Researcher. Given a topic, list 3 short factual bullet points "
        "a writer could use. Bullets only, no intro."
    )
    research = _ask(system, f"Topic: {state['topic']}")
    print("\n[researcher] produced notes:\n" + research)
    return {"research": research}

def writer(state:State)->dict:
    system = (
        "You are a Writer. Using ONLY the research notes provided, write one "
        "engaging paragraph (3-4 sentences) for a general audience."
    )
    draft = _ask(system, f"Topic: {state['topic']}\n\nResearch notes:\n{state['research']}")
    print("\n[writer] produced a draft:\n" + draft)
    return {"draft": draft}

def editor(state: State) -> dict:
    system = (
        "You are an Editor. Improve clarity and flow of the draft. Fix any awkward "
        "wording. Return ONLY the polished paragraph."
    )
    final = _ask(system, state["draft"])
    print("\n[editor] produced the final:\n" + final)
    return {"final": final}

def build_pipeline():
    g = StateGraph(State)
    g.add_node("researcher", researcher)
    g.add_node("writer", writer)
    g.add_node("editor", editor)

    g.add_edge(START, "researcher")
    g.add_edge("researcher", "writer")
    g.add_edge("writer", "editor")
    g.add_edge("editor", END)
    return g.compile()

def main() -> None:
    
    print("Sequential agents: researcher -> writer -> editor")

    pipeline = build_pipeline()

    while True:
        topic = input("\nEnter a topic (or type 'exit' to quit): ").strip()
        if topic.lower() in ("exit", "quit"):
            print("\nExiting program. Goodbye!")
            break

        if not topic:
            print("Please enter a valid topic.")
            continue

        result = pipeline.invoke(
            {
                "topic": topic,
                "research": "",
                "draft": "",
                "final": "",
            }
        )
        print(result["final"])

if __name__ == "__main__":
    main()