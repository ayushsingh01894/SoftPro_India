import os
from dotenv import load_dotenv
import streamlit as st
import db

from agent import answer_question,build_model

load_dotenv()

st.set_page_config(page_title="Chat With Your DB", page_icon=":bar_chart:")
st.title(":bar_chart: chat with your database")
st.caption("Ask question in plan english , model write and rows queries for you")

if not os.path.exists(db.DB_PATH):
    st.error("store.db not found")
    st.stop()

with st.sidebar:
    st.header("Database")
    for table in db.list_tables():
        with st.expander(table):
            st.code(db.get_schema(table), language="text")
    st.caption("Read-only. The agent can only run SELECT queries.")

if not os.getenv("GROQ_API_KEY"):
    st.warning("Api Key is not found")
    st.stop()

@st.cache_resource
def get_model():
    return build_model()

model = get_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if question := st.chat_input("e.g show me sales states ?"):
    st.session_state.messages.append(
        {
            "role":"user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        answer = answer_question(model,question)
    st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": answer,
            "steps":steps
        }
    )
