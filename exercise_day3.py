"""
A tweet can be 1–280 characters. Tell the user whether theirs is postable.

Your task: in tweet_checker.py

input() the tweet and measure it with len().
Empty first: an empty string is falsy — catch if not tweet: before anything else.
elif length ≤ 280 → "✅ Good to post! (N/280 chars)".
else → tell them how many characters over they are (length - 280).
Skills: len(), truthiness, if/elif/else, f-strings. Focus: ordering branches correctly (empty → ok → too long).

"""

#solution

tweet = input("Enter your tweet: ")

length = len(tweet)

if not tweet:
    print("❌ Tweet cannot be empty.")
elif length <= 280:
    print(f"✅ Good to post! ({length}/280 chars)")
else:
    print(f"❌ Too long! You are {length - 280} characters over the limit.")

"""
Exercise 2 — BMI Calculator 🩺
Compute Body Mass Index and classify it. BMI = weight(kg) / height(m)².

BMI	Category
< 18.5	Underweight
18.5 – 24.9	Normal
25 – 29.9	Overweight
≥ 30	Obese
Your task: in bmi_calculator.py

input() weight and height — cast with float() (height is a decimal like 1.75).
Compute bmi = weight / (height ** 2).
Use an if/elif/elif/else chain (lowest → highest) for the category.
Print the BMI to 1 decimal: f"{bmi:.1f}".
Skills: float(), **, if/elif/else ordering, f-string formatting. Focus: why the elif chain lets you write bmi < 25 without repeating bmi >= 18.5

"""

#solution

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")


"""
Exercise 3 — Rock, Paper, Scissors ✊✋✌️
Play against the computer. Rock beats scissors, scissors beats paper, paper beats rock.

Your task: in rock_paper_scissors.py

input() the player's move; .strip().lower() it (Day 2!) so "Rock" matches "rock".
Validate: if the move is not in ["rock","paper","scissors"], reject it.
Computer plays with random.choice(...). Print both moves.
Decide with if/elif/else: draw → the three player-win combos (use and/or) → else computer.
Skills: random.choice, in/not in, and/or, string methods, conditionals. Focus: combining and (within one combo) and or (across the three winning combos).
"""

import random

player = input("Choose rock, paper, or scissors: ").strip().lower()

if player not in ["rock", "paper", "scissors"]:
    print("Invalid move! Please choose rock, paper, or scissors.")
else:
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw!")
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

