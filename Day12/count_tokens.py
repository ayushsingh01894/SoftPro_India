"""
Counting tokens with Gemini.
Tokens drive cost, context limits, and speed -- so it helps to see how text
maps to token counts.
Setup: pip install google-generativeai python-dotenv  (+ GEMINI_API_KEY in .env)
Run:   python count_tokens.py 

import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file first (see the README).")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

samples = [
    "Hello",
    "I love learning about AI.",
    "Antidisestablishmentarianism",          # one long word -> several tokens
    "namaste, kaise ho aap?",                # Hindi-in-Latin often costs more
]

print("text -> token count")
for text in samples:
    count = model.count_tokens(text).total_tokens
    print(f"  {count:>3}  <- {text!r}")

print()
print("Notice: token count is NOT the same as word count or character count.")
print("Long/rare words and non-English text use more tokens.")

"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise SystemExit("Set GROQ_API_KEY in .env file")

client = Groq(api_key=api_key)

samples = [
    "Hello",
    "I love learning about AI.",
    "Antidisestablishmentarianism",
    "namaste, kaise ho aap?",
]
def prompt_tokens(test):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":"Explain what is full form of url"
            }
        ]
    )
    return response.usage.prompt_tokens

print("Text -> Response")
for text in samples:
    print(f"{prompt_tokens(text)} <--{text}")

# print("Text -> Response")
# for text in samples:
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[
#             {"role": "user", "content": text}
#         ]
#     )

#     print(f"\nInput: {text}")
#     print("Output:", response.choices[0].message.content)

#     print("Prompt tokens    :", response.usage.prompt_tokens)
#     print("Completion tokens:", response.usage.completion_tokens)
#     print("Total tokens     :", response.usage.total_tokens)