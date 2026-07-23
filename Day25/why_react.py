"""
01 - Why a ReAct agent? From a hand-written loop to one line.

On Day 23 you wrote the tool-calling loop BY HAND -- a `while` loop that:
    1. asks the model,
    2. if the model asked for a tool, runs it and feeds the result back,
    3. repeats until the model gives a plain-text answer.

That pattern has a name: ReAct = Reason + Act.

Today LangChain gives you that loop in ONE line:

    from langchain.agents import create_agent
    agent = create_agent(model, tools)

This script works completely offline by using a tiny scripted model instead
of a real LLM.
"""

from typing import List

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatResult, ChatGeneration


# ---------------------------------------------------------------------
# Tool
# ---------------------------------------------------------------------

@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b


# ---------------------------------------------------------------------
# Offline scripted model
# ---------------------------------------------------------------------

class ScriptedModel(BaseChatModel):
    """
    Tiny fake chat model.

    Instead of generating text, it simply returns pre-written AI messages
    one after another so we can watch the ReAct loop offline.
    """

    script: List[AIMessage] = []
    step: int = 0

    def bind_tools(self, tools, **kwargs):
        """
        Real chat models attach tool schemas here.

        Our fake model already knows what it wants to output,
        so we simply return self.
        """
        return self

    def _generate(
        self,
        messages,
        stop=None,
        run_manager=None,
        **kwargs,
    ):
        message = self.script[min(self.step, len(self.script) - 1)]
        object.__setattr__(self, "step", self.step + 1)

        return ChatResult(
            generations=[
                ChatGeneration(message=message)
            ]
        )

    @property
    def _llm_type(self):
        return "scripted-offline"


# ---------------------------------------------------------------------
# Script (Reason -> Act -> Observe -> Answer)
# ---------------------------------------------------------------------

script = [

    # Step 1
    AIMessage(
        content="",
        tool_calls=[
            {
                "name": "add",
                "args": {
                    "a": 240,
                    "b": 360,
                },
                "id": "call_1",
            }
        ],
    ),

    # Step 2
    AIMessage(
        content="240 + 360 = 600."
    ),
]


# ---------------------------------------------------------------------
# Create the ReAct agent
# ---------------------------------------------------------------------

agent = create_agent(
    model=ScriptedModel(script=script),
    tools=[add],
)


# ---------------------------------------------------------------------
# Ask a question
# ---------------------------------------------------------------------

print("Asking the agent:")
print("What is 240 + 360?\n")

result = agent.invoke(
    {
        "messages": [
            ("human", "What is 240 + 360?")
        ]
    }
)


# ---------------------------------------------------------------------
# Display the ReAct loop
# ---------------------------------------------------------------------

print("=" * 60)
print("Full ReAct Message Trail")
print("=" * 60)

for message in result["messages"]:
    message_type = type(message).__name__
    if getattr(message, "tool_calls", None):
        tool_call = message.tool_calls[0]
        print(
            f"{message_type:14} -> ACT: "
            f"{tool_call['name']}({tool_call['args']})"
        )
    elif message_type == "ToolMessage":
        print(
            f"{message_type:14} -> "
            f"OBSERVE: tool returned {message.content}"
        )
    elif message.content:
        print(
            f"{message_type:14} -> {message.content}"
        )

print("\n" + "=" * 60)
print("Final Answer")
print("=" * 60)

print(result["messages"][-1].content)

print("\nEverything above happened because of this single line:\n")
print("agent = create_agent(model, tools)")