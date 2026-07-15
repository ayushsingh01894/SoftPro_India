import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="messages")
])

chain = prompt | llm | StrOutputParser()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("AI Chatbot")

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    response = chain.invoke({
        "messages": st.session_state.messages
    })

    st.session_state.messages.append(
        AIMessage(content=response)
    )

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    else:
        with st.chat_message("assistant"):
            st.write(msg.content)