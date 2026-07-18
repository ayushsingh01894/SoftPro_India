from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import datetime
import math

load_dotenv()

# 1. Define multiple tools

@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

@tool
def divide_numbers(a: float, b: float) -> str:
    """Divide a by b. Returns an error message if b is 0."""
    if b == 0:
        return "Error: division by zero"
    return str(a / b)

@tool
def square_root(a: float) -> str:
    """Calculate the square root of a number."""
    if a < 0:
        return "Error: cannot take square root of a negative number"
    return str(math.sqrt(a))

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city (demo data)."""
    fake_data = {
        "delhi": "32°C, hazy",
        "lucknow": "34°C, sunny",
        "mumbai": "29°C, humid",
        "bangalore": "24°C, rainy"
    }
    return fake_data.get(city.lower(), f"No weather data found for {city}")

@tool
def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def word_count(text: str) -> int:
    """Count the number of words in a given piece of text."""
    return len(text.split())

# 2. Initialize Groq LLM

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# 3. Register all tools

tools = [
    add_numbers,
    multiply_numbers,
    divide_numbers,
    square_root,
    get_weather,
    get_current_time,
    word_count
]

agent = create_react_agent(llm, tools=tools)

# 4. Interactive chat loop

def main():
    print("🤖 Multi-Tool Groq Agent — type 'exit' to quit\n")
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        chat_history.append(("user", user_input))

        response = agent.invoke({"messages": chat_history})
        # Extract the final AI message
        final_message = response["messages"][-1].content
        print(f"Agent: {final_message}\n")
        chat_history.append(("assistant", final_message))

if __name__ == "__main__":
    main()