"""
Exercise 1 — Number Guessing Game 🎯
The computer picks a secret number 1–100; the player guesses until they get it.

Your task: in guessing_game.py

import random and pick secret = random.randint(1, 100).
Loop with while True: — ask for a guess each round and int()-cast it.
Tell them "Too high" / "Too low" / "Correct!" using if/elif/else.
break when they're right; count attempts and print them at the end.
Skills: while True, break, random.randint, comparisons, an accumulator (attempt counter). Focus: the while True + break idiom — loop until the win condition, then leave.

"""
#solution
import random

secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break

print(f"You guessed the number in {attempts} attempts.")

"""
Exercise 3 — Multiplication Table 🔢
Print a clean, aligned multiplication grid up to N × N using nested loops.

Your task: in multiplication_table.py

Outer for over rows 1..N, inner for over columns 1..N.
Build each row (inner loop), then print() it — newline after the inner loop.
Align columns with an f-string width like f"{value:>4}" so it lines up.
Skills: nested for loops, range, f-string alignment, "build a row" pattern. Focus: row/column flow — where the per-row print() goes, and why alignment needs a fixed width.

"""
#solution

N = int(input("Enter table size: "))

for row in range(1, N + 1):
    line = ""

    for col in range(1, N + 1):
        value = row * col
        line += f"{value:>4}"

    print(line)

    """
    Exercise 2 — FizzBuzz 🍷
The famous interview screen. Print numbers 1..N, but:

multiples of 3 → "Fizz"
multiples of 5 → "Buzz"
multiples of both 3 and 5 → "FizzBuzz"
Your task: in fizzbuzz.py

for n in range(1, N + 1): (remember: stop is exclusive!).
Check n % 15 == 0 FIRST (or build the string) — order matters, this is the classic trap.
Otherwise % 3, then % 5, else the number itself.
Skills: for, range, the modulo operator %, if/elif/else ordering. Focus: why you must test "divisible by both" before the individual cases.

➡ Solution: fizzbuzz_solution.py
    
    """

#solution
N = int(input("Enter N: "))

for n in range(1, N + 1):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)