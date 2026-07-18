"""
agent.py -- the brain of the project.  (STARTER -- finish the TODOs)

This is the module-04 tool-calling loop, pointed at the database tools. The
SHAPE of the loop is the whole lesson:

    model -> (list_tables) -> model -> (describe_table) -> model
          -> (run_sql_query) -> model -> final English answer

The model keeps asking for tools until it has enough to answer. You write that
loop in answer_question() below.

The system prompt, the offline stand-in model, and build_model() are done for
you -- so you can run this file with NO key and watch YOUR loop drive the
offline model through a real 3-tool sequence.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python build_sample_db.py   # once, to create store.db
    python agent.py             # a demo question (offline if you have no key)
"""

import os
from dotenv import load_dotenv
from langchain_core.messages import (SystemMessage, HumanMessage, AIMessage,
                                     ToolMessage)

from tools import TOOLS, TOOL_MAP   # you built these in tools.py

load_dotenv()
MODEL = "llama-3.1-8b-instant"
MAX_STEPS = 8   # safety cap: at most this many model<->tool round-trips
MAX_TOKEN=4000
SYSTEM_PROMPT = (
    "You are a helpful data analyst for an online store. You answer questions by "
    "querying a SQLite database with the tools provided. Follow this process:\n"
    "1. Call list_tables to see what tables exist.\n"
    "2. Call describe_table on the tables you need, to learn the exact columns.\n"
    "3. Call run_sql_query with a single read-only SELECT to get the data.\n"
    "4. Read the rows and answer the user in plain English with the numbers.\n"
    "Never invent table or column names -- always check with the tools first. "
    "If a query errors, read the error and try a corrected query."
)


def answer_question(model, question, verbose=True, on_tool=None):
    """
    Run the tool-calling loop and return the model's final text answer.

    on_tool: optional callback(name, args, result) fired for each tool call.
    The Streamlit app uses it to show the agent's steps; the CLI uses verbose.
    """
    # Start the conversation: the system instructions + the user's question.
    messages = [SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=question)]
    
    for _ in range(MAX_STEPS):
        ai = model.invoke(messages)
        messages.append(ai)
        if not ai.tool_calls:
            return ai.content
        for call in ai.tool_calls:
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            messages.append(ToolMessage(content=str(result),tool_call_id=call["id"]))


def build_model():
    """Return a Groq model bound to our DB tools (requires GROQ_API_KEY)."""
    from langchain_groq import ChatGroq
    return ChatGroq(model=MODEL, temperature=0).bind_tools(TOOLS)


# ----------------------------------------------------------------------------
# Offline stand-in (DONE for you): scripts a real 3-tool sequence for one demo
# question, so you can test your loop with no key. It is NOT an LLM -- it just
# replays fixed steps based on how many tools have run so far.
# ----------------------------------------------------------------------------
class OfflineDBModel:
    def invoke(self, messages):
        tool_results = [m for m in messages if isinstance(m, ToolMessage)]
        n = len(tool_results)
        if n == 0:
            return AIMessage(content="", tool_calls=[
                {"name": "list_tables", "args": {}, "id": "c1"}])
        if n == 1:
            return AIMessage(content="", tool_calls=[
                {"name": "describe_table", "args": {"table_name": "customers"},
                 "id": "c2"}])
        if n == 2:
            return AIMessage(content="", tool_calls=[
                {"name": "run_sql_query",
                 "args": {"query": "SELECT COUNT(*) FROM customers WHERE city='Pune'"},
                 "id": "c3"}])
        count = tool_results[-1].content.splitlines()[-1]
        return AIMessage(
            content=f"There are {count} customers from Pune. "
                    f"(Offline stand-in: with a Groq key, a real model answers "
                    f"any question you type.)")


if __name__ == "__main__":
    if os.getenv("GROQ_API_KEY"):
        model = build_model()
        demo_questions = [
            "How many customers are from Pune?",
            "Which product category has the most products?",
            "What are our 3 most expensive products?",
        ]
        print("Using real Groq model.\n")
    else:
        model = OfflineDBModel()
        demo_questions = ["How many customers are from Pune?"]
        print("No GROQ_API_KEY -- using an OFFLINE stand-in to demo the loop.\n")

    for q in demo_questions:
        print(f"Q: {q}")
        print(f"A: {answer_question(model, q)}\n")
