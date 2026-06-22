"""
A tiny decision cheat-sheet for picking a model (no API key needed).

Run:
    python model_cheatsheet.py


# (need, recommendation) pairs -- a starting-point heuristic, not a hard rule.
cheatsheet = [
    ("Most everyday tasks (fast + free)", "Gemini gemini-2.0-flash"),
    ("Hard reasoning / long complex work", "Gemini gemini-2.5-pro"),
    ("Lowest latency (very fast replies)", "Groq (hosted open models)"),
    ("Offline / private / no rate limits", "Ollama on your laptop"),
    ("A rare/specialised open model", "Hugging Face Inference"),
]

print("What you need ->  Reach for")
print("-" * 55)
for need, pick in cheatsheet:
    print(f"  {need:38} {pick}")

print()
print("Rule of thumb: start with Gemini flash; switch only for a concrete")
print("reason (speed, privacy, quality). Day 12 makes switching one line.")


"""

"""
A tiny decision cheat-sheet for picking a model.

Run:
    python model_cheatsheet.py
"""

cheatsheet = [
    ("Most everyday tasks (fast + free)", "Llama 3.1 8B Instant (Groq)"),
    ("Best quality on Groq", "Llama 3.3 70B Versatile"),
    ("Reasoning / math / coding", "DeepSeek R1 Distill Llama 70B"),
    ("Lowest latency", "Groq hosted models"),
    ("Offline / private / no API costs", "Ollama on your laptop"),
    ("Huge open-source model collection", "Hugging Face Inference"),
]

print("What you need              ->  Reach for")
print("-" * 60)

for need, pick in cheatsheet:
    print(f"{need:38} {pick}")

print()
print("Rule of thumb:")
print("Start with Llama 3.3 70B Versatile.")
print("Switch only for a specific reason:")
print("- Need more speed? -> Llama 3.1 8B Instant")
print("- Need reasoning? -> DeepSeek R1 Distill")
print("- Need privacy? -> Ollama")