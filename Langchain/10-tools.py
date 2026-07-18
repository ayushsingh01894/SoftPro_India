from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b

@tool
def word_count(text: str) -> int:
    """Count how many words are in a text."""
    return len(text.split())

print("=" * 60)
print("What the model sees about each tool")
print("=" * 60)

for t in (multiply, word_count):
    print(f"name : {t.name}")
    print(f"description : {t.description}")
    print(f"args : {t.args}")
    print("=" * 60)

print(multiply.invoke({"a":6,"b":3}))
print(word_count.invoke({"text":"tools in the files"}))