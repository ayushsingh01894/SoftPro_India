# Prompting = is the process of giving instructions or input (called a prompt) to an AI model so that it generates the desired output.

"""

systems prompts 

Types of Prompting

Zero-shot prompting: Ask the AI directly without examples.

Translate "Hello" into French.

One-shot prompting: Give one example before asking.
Example:
English: Cat
Hindi: बिल्ली
English: Dog

Few-shot prompting: Give multiple examples so the AI learns the pattern.

English: Cat → बिल्ली
English: Dog → कुत्ता
English: Bird → ?

Chain-of-thought prompting (for reasoning tasks): Encourage step-by-step reasoning. For example:

Solve this math problem by explaining your reasoning.
(Modern reasoning models may reason internally even without explicitly showing every intermediate step.)

"""

import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"


def generate(title, messages):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
    )

    print(response.choices[0].message.content)


# ------------------------------------------------------------------
# 1. ZERO SHOT PROMPTING
# ------------------------------------------------------------------

generate(
    "1. ZERO SHOT PROMPTING",
    [
        {
            "role": "user",
            "content": "Explain Python in simple words."
        }
    ]
)

# ------------------------------------------------------------------
# 2. ONE SHOT PROMPTING
# ------------------------------------------------------------------

generate(
    "2. ONE SHOT PROMPTING",
    [
        {
            "role": "user",
            "content": """
Example

English : Apple
Hindi : सेब

Translate

English : Mango
"""
        }
    ]
)

# ------------------------------------------------------------------
# 3. FEW SHOT PROMPTING
# ------------------------------------------------------------------

generate(
    "3. FEW SHOT PROMPTING",
    [
        {
            "role": "user",
            "content": """
Translate English to Hindi.

Examples

Apple -> सेब
Mango -> आम
Orange -> संतरा

Translate

Banana ->
"""
        }
    ]
)

# ------------------------------------------------------------------
# 4. SYSTEM PROMPTING
# ------------------------------------------------------------------

generate(
    "4. SYSTEM PROMPTING",
    [
        {
            "role": "system",
            "content": "You are a Python teacher. Explain every topic with examples."
        },
        {
            "role": "user",
            "content": "What is a Python function?"
        }
    ]
)

# ------------------------------------------------------------------
# 5. ROLE PROMPTING
# ------------------------------------------------------------------

generate(
    "5. ROLE PROMPTING",
    [
        {
            "role": "system",
            "content": "You are an HR interviewer."
        },
        {
            "role": "user",
            "content": "Ask me five Python interview questions."
        }
    ]
)

# ------------------------------------------------------------------
# 6. PERSONA PROMPTING
# ------------------------------------------------------------------

generate(
    "6. PERSONA PROMPTING",
    [
        {
            "role": "system",
            "content": "You are a funny teacher who explains with simple examples."
        },
        {
            "role": "user",
            "content": "Explain Artificial Intelligence."
        }
    ]
)

# ------------------------------------------------------------------
# 7. INSTRUCTION PROMPTING
# ------------------------------------------------------------------

generate(
    "7. INSTRUCTION PROMPTING",
    [
        {
            "role": "user",
            "content": """
Explain Machine Learning.

Rules:
1. Maximum 100 words.
2. Use bullet points.
3. Give one real-life example.
"""
        }
    ]
)

# ------------------------------------------------------------------
# 8. CONTEXT PROMPTING
# ------------------------------------------------------------------

generate(
    "8. CONTEXT PROMPTING",
    [
        {
            "role": "user",
            "content": """
Context:
I am a beginner learning Python.

Question:
Explain loops.
"""
        }
    ]
)

# ------------------------------------------------------------------
# 9. OUTPUT FORMAT PROMPTING
# ------------------------------------------------------------------

generate(
    "9. OUTPUT FORMAT PROMPTING",
    [
        {
            "role": "user",
            "content": """
Explain Python Data Types.

Return the answer in Markdown table format.

Columns:
Data Type
Description
Example
"""
        }
    ]
)

# ------------------------------------------------------------------
# 10. REASONING PROMPT
# ------------------------------------------------------------------

generate(
    "10. REASONING PROMPT",
    [
        {
            "role": "user",
            "content": """
Solve this problem and explain your reasoning.

A train travels 240 km in 4 hours.
What is its speed?
"""
        }
    ]
)

# ------------------------------------------------------------------
# 11. JSON PROMPTING
# ------------------------------------------------------------------

generate(
    "11. JSON PROMPTING",
    [
        {
            "role": "user",
            "content": """
Explain Python.

Return ONLY JSON.

{
    "language":"",
    "creator":"",
    "released":"",
    "uses":[]
}
"""
        }
    ]
)

# ------------------------------------------------------------------
# 12. CONVERSATION PROMPTING
# ------------------------------------------------------------------

generate(
    "12. CONVERSATION PROMPTING",
    [
        {
            "role": "system",
            "content": "You are a Python teacher."
        },
        {
            "role": "user",
            "content": "What is Python?"
        },
        {
            "role": "assistant",
            "content": "Python is a popular programming language."
        },
        {
            "role": "user",
            "content": "What are its advantages?"
        }
    ]
)

print("\n" + "=" * 80)
print("All prompting examples executed successfully!")
print("=" * 80)