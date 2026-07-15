import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="wide"
)

load_dotenv()

@st.cache_resource
def get_client():
    if not os.getenv("GROQ_API_KEY"):
        return None
    return Groq(api_key= os.environ.get("GROQ_API_KEY"))

client = get_client()

if client is None:
    st.error("GROQ_API_KEY not found. Please check your .env file.")
    st.stop()

st.sidebar.header("Settings")
model = st.sidebar.selectbox(
    "Model",
    ["llama-3.1-8b-instant","llama-3.3-70b-versatile"]
)
if st.sidebar.button('Clear Chat'):
    st.session_state.messages =[]
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    

user_text = st.chat_input("Type your message...")
if user_text:
    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_text
        }
    )

    with st.chat_message("user"):
        st.markdown(user_text)
    
    # ask groq for a reply
    with st.chat_message("assistant"):
        messages_to_send = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]

        messages_to_send.extend(st.session_state.messages)

        stream = client.chat.completions.create(
            model=model,
            messages=messages_to_send,
            temperature=0.4,
            stream=True
        )

        reply = st.write_stream(
            chunk.choices[0].delta.content or ""
            for chunk in stream
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )