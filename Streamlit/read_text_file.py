from pathlib import Path

SAMPLE = Path(__file__).resolve().parent / "hello.txt"

def read_whole_file() -> str:
    with open(SAMPLE, "r", encoding="utf-8") as f:
        return f.read()

print(read_whole_file())


def read_line() -> str:
    with open(SAMPLE , "r" , encoding="utf-8") as f:
        return f.readlines(1)

print(read_line())

def read_line_by_line() -> str:
    with open(SAMPLE , "r" , encoding="utf-8") as f:
        for number, line in enumerate(f,start=1):
            print(f" line {number} : {line} ")
print(read_line_by_line())

def write_file(text: str):
    """Overwrite the file with new text."""
    with open(SAMPLE, "w", encoding="utf-8") as f:
        f.write(text)


# Write to the file
write_file("Hello, Python!\nThis is a new line.")

print("\nAfter writing:")
print(read_whole_file())