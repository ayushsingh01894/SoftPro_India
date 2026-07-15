import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq

load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

# Store histories
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

session_id = "user1"

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    response = chatbot.invoke(
        {"input": question},
        config={"configurable": {"session_id": session_id}}
    )
    print("AI:", response)