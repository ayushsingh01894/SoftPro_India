from typing import TypedDict, Annotated
from operator import add

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.graph.message import add_messages


class NoReducer(TypedDict):
    log: list


def step_a(state):
    return {"log": ["Step A executed"]}


def step_b(state):
    return {"log": ["Step B executed"]}


class WithReducer(TypedDict):
    log: Annotated[list, add]


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


def user_turn(state):
    text = input("You: ")
    return {"messages": [("human", text)]}


def bot_turn(state):
    last = state["messages"][-1].content
    return {"messages": [("ai", f"You said: {last}")]} 


class AgentState(MessagesState):
    step_count: int


def run_part_a():
    builder = StateGraph(NoReducer)

    builder.add_node("step_a", step_a)
    builder.add_node("step_b", step_b)

    builder.add_edge(START, "step_a")
    builder.add_edge("step_a", "step_b")
    builder.add_edge("step_b", END)

    graph = builder.compile()

    result = graph.invoke({"log": []})

    print("\nResult:")
    print(result["log"])


def run_part_b():
    builder = StateGraph(WithReducer)

    builder.add_node("step_a", step_a)
    builder.add_node("step_b", step_b)

    builder.add_edge(START, "step_a")
    builder.add_edge("step_a", "step_b")
    builder.add_edge("step_b", END)

    graph = builder.compile()

    result = graph.invoke({"log": []})

    print("\nResult:")
    print(result["log"])


def run_part_c():
    builder = StateGraph(ChatState)

    builder.add_node("user_turn", user_turn)
    builder.add_node("bot_turn", bot_turn)

    builder.add_edge(START, "user_turn")
    builder.add_edge("user_turn", "bot_turn")
    builder.add_edge("bot_turn", END)

    graph = builder.compile()

    result = graph.invoke({"messages": []})

    print("\nConversation:")

    for msg in result["messages"]:
        print(f"{msg.type}: {msg.content}")


def run_part_d():
    print("\nMessagesState fields:")
    print(MessagesState.__annotations__)

    print("\nAgentState fields:")
    print(AgentState.__annotations__)


while True:

    print("\n========== Reducer Demo ==========")
    print("1. No Reducer")
    print("2. List Reducer (add)")
    print("3. add_messages")
    print("4. MessagesState")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        run_part_a()

    elif choice == "2":
        run_part_b()

    elif choice == "3":
        run_part_c()

    elif choice == "4":
        run_part_d()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


"""

What you'll observe
Choice 1 (No Reducer)
Result:
['Step B executed']
step_b overwrites step_a.

Choice 2 (Reducer using add)
Result:
['Step A executed', 'Step B executed']
The reducer concatenates the lists.

Choice 3 (add_messages)
You: Hello
Conversation:
human: Hello
ai: You said: Hello
add_messages converts tuples like ("human", "...") into proper LangChain message objects.

Choice 4 (MessagesState)
Displays the built-in fields of MessagesState and your extended AgentState.
This interactive version makes it much easier to understand the difference between overwriting state, using reducers, and working with chat messages.

"""