import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise RuntimeError("GROQ_API_KEY not found in .env file.")

client = Groq(api_key=API_KEY)

MODEL = "llama-3.3-70b-versatile"

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "Give clear and concise answers."
        ),
    }
]

print("=" * 60)
print("🤖 Groq CLI Chatbot")
print("Type 'exit', 'quit', or 'bye' to end the chat.")
print("=" * 60)

while True:
    try:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nAssistant: Goodbye! 👋")
            break

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_completion_tokens=1024,
        )

        reply = response.choices[0].message.content

        print(f"\nAssistant: {reply}")

        messages.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )

    except KeyboardInterrupt:
        print("\n\nAssistant: Goodbye! 👋")
        break

    except Exception as e:
        print(f"\nError: {e}")

