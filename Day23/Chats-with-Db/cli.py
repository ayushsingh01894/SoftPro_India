"""
cli.py -- chat with your database from the terminal.

Once answer_question() works in agent.py, the CLI is a thin loop around it:
read a question, print the answer, repeat.

Setup:
    pip install langchain langchain-groq python-dotenv
    # put GROQ_API_KEY=... in a .env file in this folder

Run:
    python build_sample_db.py   # once
    python cli.py
"""

import os
from dotenv import load_dotenv
from agent import answer_question, build_model, OfflineDBModel

# Load environment variables from .env
load_dotenv()


def main():
    print("  Chat With Your Database (type 'quit' to exit)")

    # If no API key, run one offline demo.
    if not os.getenv("GROQ_API_KEY"):
        print("No GROQ_API_KEY found -- running ONE offline demo question.\n")
        model = OfflineDBModel()
        question = "How many customers are from Pune?"
        print(f"You: {question}")
        print(f"Bot: {answer_question(model, question, verbose=False)}\n")

        print("Add a free Groq API key to a .env file to ask your own questions.")
        return

    # Build the Groq model
    model = build_model()
    print("Ask about customers, products, orders.")
    print("Example: Which city has the most customers?\n")

    while True:
        try:
            question = input("YOU : ").strip()
            if not question:
                continue
            if question.lower() in ("quit", "exit", "bye"):
                print("Goodbye!")
                break
            answer = answer_question(model, question)
            print(f"Bot: {answer}\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()