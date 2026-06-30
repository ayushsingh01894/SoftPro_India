import os
import json
from dotenv import load_dotenv
from groq import Groq

# .env file se environment variables load karo
load_dotenv()

MODEL = "llama-3.3-70b-versatile"
HISTORY_FILE = "chat_history.json"
SYSTEM_PROMPT = "You are a friendly, concise and clear assistant. Keep replies short and simple."


def save(messages: list) -> None:
    # Chat history ko file me save karo
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

    print(f"Bot : saved {len(messages)} messages in {HISTORY_FILE}.\n")


def load() -> list:
    try:
        # File se purani chat history load karo
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            messages = json.load(f)
        print(f"Bot : loaded {len(messages)} messages from {HISTORY_FILE}.\n")
        return messages
    except FileNotFoundError:
        print()


def fresh_history() -> list:
    # Nayi conversation start karo sirf system prompt ke sath
    return [{"role": "system", "content": SYSTEM_PROMPT}]


def main() -> None:
    # Groq client banao
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    # Starting me fresh history lo
    messages = fresh_history()

    print("Chatbot ready. Commands: /reset /history /save /load /exit\n")

    while True:
        user_text = input("You : ").strip()

        # Empty input ignore karo
        if not user_text:
            continue

        cmd = user_text.lower()

        # Chat band karne ke liye
        if cmd in {"/exit", "/quit"}:
            print("Bot : Bye!")
            break

        # Chat reset karne ke liye
        if cmd == "/reset":
            messages = fresh_history()
            print("Bot : conversation cleared.\n")
            continue

        # Chat save karne ke liye
        if cmd == "/save":
            save(messages)
            continue

        # Saved chat load karne ke liye
        if cmd == "/load":
            messages = load()
            continue
        
        if cmd == "/history":
            # Ab tak ki saari chat history dikhao
            print("\n----- Chat History -----")
            for msg in messages:
                print(f"{msg['role'].capitalize()} : {msg['content']}")
            print("------------------------\n")
            continue

        # User ka message history me add karo
        messages.append({"role": "user", "content": user_text})

        # Model se response lo
        chat = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        # Bot ka reply nikalo
        reply = chat.choices[0].message.content.strip()

        # Reply bhi history me save karo
        messages.append({"role": "assistant", "content": reply})

        # Reply print karo
        print("Bot :", reply, "\n")


if __name__ == "__main__":
    # Program yahin se start hoga
    main()