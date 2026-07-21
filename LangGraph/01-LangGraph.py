# make first example and run wihout ai 
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text:str

# A node is just a function that takes current state and returns dict of key it needs to update

def shout(state:State) -> dict:
    return {"text": state["text"].upper() + " !"}


builder = StateGraph(State)
builder.add_node("Shout",shout)
builder.add_edge(START,"Shout")
builder.add_edge("Shout",END)

graph = builder.compile()
result = graph.invoke({"text":"hello langgraph"})
print("input : hello langgraph")
print("Output:", result)
print("Just the text:", result["text"])
print()