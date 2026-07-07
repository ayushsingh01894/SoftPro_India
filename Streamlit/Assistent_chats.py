import os
import json
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Configuration

st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="wide"
)

load_dotenv()

MODEL = "llama-3.3-70b-versatile"
HISTORY_FILE = "chat_history.json"

SYSTEM_PROMPT = """
You are an intelligent AI assistant.

Guidelines:
- Give accurate and well-structured answers.
- Explain concepts step by step when needed.
- If the user asks a simple question, answer briefly.
- If the user asks for code, provide clean, commented code.
- If you don't know something, say so.
- Use markdown formatting.
- Give examples whenever useful.
- Be friendly and professional.
"""

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Functions

def fresh_history():
    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


def save_chat(messages):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)


def load_chat():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return fresh_history()


# Session State

if "messages" not in st.session_state:
    st.session_state.messages = fresh_history()

# Sidebar

with st.sidebar:

    st.title("Settings")

    temperature = st.slider(
        "Temperature",
        0.0,
        1.5,
        0.7,
        0.1
    )

    max_tokens = st.slider(
        "Max Tokens",
        256,
        4096,
        2048,
        256
    )

    st.divider()

    if st.button("Reset Chat", use_container_width=True):
        st.session_state.messages = fresh_history()
        st.rerun()

    if st.button("Save Chat", use_container_width=True):
        save_chat(st.session_state.messages)
        st.success("Chat Saved!")

    if st.button("Load Chat", use_container_width=True):
        st.session_state.messages = load_chat()
        st.success("Chat Loaded!")
        st.rerun()

    if st.button("Show History", use_container_width=True):
        st.json(st.session_state.messages)

# Title

st.title("Groq Chatbot")

# Display Previous Messages

for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input

prompt = st.chat_input("Type your message...")

if prompt:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Message
    with st.chat_message("assistant"):

        placeholder = st.empty()
        full_response = ""

        stream = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                placeholder.markdown(full_response + "| ")
        placeholder.markdown(full_response)

    # Save assistant reply
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )

    # Keep only recent history
    MAX_HISTORY = 12

    if len(st.session_state.messages) > MAX_HISTORY + 1:
        st.session_state.messages = (
            [st.session_state.messages[0]]
            + st.session_state.messages[-MAX_HISTORY:]
        )


"""
Program Start
      │
      ▼
Import Libraries
      │
      ▼
Load API Key
      │
      ▼
Create Groq Client
      │
      ▼
Initialize Session
      │
      ▼
Create Sidebar
      │
      ▼
Show Previous Chats
      │
      ▼
Wait For User Input
      │
      ▼
User types message
      │
      ▼
Send to Groq
      │
      ▼
Receive Streaming Response
      │
      ▼
Display Response
      │
      ▼
Save Response in Session

"""