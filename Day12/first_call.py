"""
Your first Gemini API call.

Setup:
    pip install google-generativeai python-dotenv
    # put GEMINI_API_KEY=... in a .env file (get a free key at aistudio.google.com/apikey)
Run:
    python first_call.py
    
"""
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file first (see the README).")

genai.configure(api_key=api_key)

# gemini-2.0-flash: fast and free. (Model names change -- see the README.)
model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Explain what an API is in one simple sentence.")

print("Model's answer:")
print(response.text)

# The response also carries token usage -- handy for cost/limits later.
usage = response.usage_metadata
print()
print("Prompt tokens    :", usage.prompt_token_count)
print("Response tokens  :", usage.candidates_token_count)
print("Total tokens     :", usage.total_token_count)



"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise SystemExit("Set GROQ_API_KEY in your .env file")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is in one simple sentence."
        }
    ],
    temperature=0.7,
)

print("Model's answer:")
print(response.choices[0].message.content)

# Usage information
print("\nPrompt tokens   :", response.usage.prompt_tokens)
print("Completion tokens:", response.usage.completion_tokens)
print("Total tokens    :", response.usage.total_tokens)
