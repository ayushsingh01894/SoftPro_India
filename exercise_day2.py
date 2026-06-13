"""
Exercise 1 — Age Calculator 🎂
Ask the user for their name and birth year, then tell them how old they'll turn this year.

Your task: in age_calculator.py

input() their name and birth year (remember: input is a string).
Cast the year with int() and compute age = 2026 - birth_year.
Print a friendly message using an f-string, e.g. Hi Riya, you turn 25 in 2026!
Skills: input(), int(), f-strings.
"""
# solution ---

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

print(f"Hi {name}, you turn {age} in 2026!")
"""
Exercise 2 — Shopping Cart 🛒
Build a tiny receipt for an online order (₹ amounts), formatted neatly.

Your task: in shopping_cart.py, with these values already given:

item = "Wireless Mouse", price = 799.0, quantity = 3, gst_rate = 0.18
Compute subtotal, gst (subtotal × rate), and total, then print a receipt where every amount shows 2 decimals and a thousands separator, e.g. Rs 2,397.00. Use f-string formatting (:,.2f). (Print Rs, not ₹ — the default Windows console can't display the rupee symbol.)

Skills: f-strings, :,.2f and :.0% formatting. """

# solution
item = "Wireless Mouse"
price = 799.0
quantity = 3
gst_rate = 0.18

subtotal = price * quantity
gst = subtotal * gst_rate
total = subtotal + gst

print("===== RECEIPT =====")
print(f"Item: {item}")
print(f"Price: Rs {price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: Rs {subtotal:,.2f}")
print(f"GST Rate: {gst_rate:.0%}")
print(f"GST: Rs {gst:,.2f}")
print(f"Total: Rs {total:,.2f}") 

"""
Exercise 3 — Press Release 📰
A junior intern pasted a messy headline. Clean it up with string methods.

Your task: in press_release.py, starting from raw = "   softpro school of ai LAUNCHES new 45-day ai program!!!   " produce a tidy headline:

.strip() the surrounding spaces
.replace("!!!", "") to drop the extra punctuation
.title() to capitalise each word
Do it as one chained expression, then print the before and after.
Bonus: print how many characters were removed (len(raw) vs len(clean)).

Skills: .strip(), .replace(), .title(), method chaining, len().
"""

#solution

raw = "   softpro school of ai LAUNCHES new 45-day ai program!!!   "

clean = raw.strip().replace("!!!", "").title()

print("Before:", raw)
print("After :", clean)

print("Characters removed:", len(raw) - len(clean))
