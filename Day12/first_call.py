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
        # {
        #     # #set role means direct role dena when u builind some .
        #     # "role":"system",
        #     # #content are use to set a role like ai kaisa anser dega ?
        #     # "content":"You are a 5 year old kid. who answer everything as a joke"
        # }
        
        {
            "role":"user",
            "content":"Explain what is full form of url"
        }
    ]
)
print("Model response ")
print(response.choices[0].message.content)

#usege = response.usages
print()
print("\nPrompt tokens   :", response.usage.prompt_tokens) # input tokens 
print("Completion tokens:", response.usage.completion_tokens) # output tokens
print("Total tokens    :", response.usage.total_tokens)



