"""
low temp - 0.1 ,0.2 = same answer ayega pridictable output
hing when  1.0 , 1.2  = not same every time changes  , when u want something like creative then use high tempretures 

"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise SystemExit("Set GROQ_API_KEY in your .env file.")

client = Groq(api_key=api_key)

prompt = "Suggest a creative name for an AI tutoring app. Reply with just the name."

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=20,
 )

app_name = response.choices[0].message.content
print(app_name)

