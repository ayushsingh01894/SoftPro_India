import os

from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

MODEL = "llama-3.3-70b-versatile"
SYSTEM_PROMPT = (
    "You are sparky, a cheerful coding tutor for indian mca student who known about basic python and explain simply , use small example and keep it under 3 sentences "
)
def main() -> None:
    # Create Groq client using API key
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    # Store conversation history
    messages = [{"role":"system","content":SYSTEM_PROMPT}]

    print("Sparky is ready . Type /quit to exit.\n")

    while True:
        user_text = input("You : ").strip()

        # Exit the chatbot
        if user_text.lower() in {"/exit", "/quit"}:
            print("Bot : Bye!")
            break

        # Ignore empty input
        if not user_text:
            continue

        # Add user's message to the history
        messages.append({"role": "user", "content": user_text})

        # Send conversation history to the model
        chat = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        # Get bot's reply
        reply = chat.choices[0].message.content.strip()

        # Add bot's reply too, so it remembers what was said
        messages.append({"role": "assistant", "content": reply})

        # Print bot response
        print("Bot :", reply, "\n")


if __name__ == "__main__":
    # Start the chatbot
    main()
