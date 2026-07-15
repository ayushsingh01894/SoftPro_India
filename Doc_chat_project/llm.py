import os
from groq import Groq


def make_client():
    if not os.getenv("GROQ_API_KEY"):
        return None
    return Groq()


def stream_answer(client, model: str, messages: list, temperature: float, max_tokens: int):
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,   # send the answer in pieces as it is produced
    )
    for chunk in stream:
        piece = chunk.choices[0].delta.content
        if piece:
            yield piece


def complete_answer(client, model: str, messages: list,temperature: float, max_tokens: int) -> str:

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content or ""

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    client = make_client()
    if client is None:
        print("No GROQ_API_KEY set - skipping live test (this is fine).")
    else:
        msgs = [{"role": "user", "content": "Say 'llm.py works' and nothing else."}]
        print(complete_answer(client, "llama-3.1-8b-instant", msgs, 0.0, 20))