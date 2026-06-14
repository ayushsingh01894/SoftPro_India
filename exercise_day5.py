"""
Exercise 1 — Temperature Converter 🌡️
Write two small functions and use their return values together.

Your task: in temperature_converter.py

def c_to_f(c): → return c * 9 / 5 + 32.
def f_to_c(f): → return (f - 32) * 5 / 9.
input() a Celsius value, float()-cast it, call c_to_f, and print the result to 1 decimal.
Round-trip check: feed the result back into f_to_c and confirm you get the original.
Skills: def, one parameter, return, composing functions, f-string formatting. Focus: using a returned value (not printing inside the function) — return, not print.

"""
#solution

def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


celsius = float(input("Enter a Celsius value: "))

fahrenheit = c_to_f(celsius)
print(f"{fahrenheit:.1f}")

# Round-trip check
celsius_again = f_to_c(fahrenheit)
print(f"{celsius_again:.1f}")


"""
Exercise 2 — Password Strength Checker 🔐
Write a function that returns a strength verdict, with a tunable minimum length via a default arg.

Your task: in password_checker.py

def check_password(pw, min_length=8): — return a string verdict, don't print inside.
Score points for: length ≥ min_length, has a digit, has an uppercase, has a symbol. (Hint: any(ch.isdigit() for ch in pw), ch.isupper(), and a set of symbols.)
Map score → "weak" / "medium" / "strong" and return it.
input() a password and print the verdict. Try calling with min_length=12 too.
Skills: def, return, default arguments, booleans, any(), string methods. Focus: the function returns data; the caller decides what to do with it.

"""
#solution

def check_password(pw, min_length=8):
    symbols = set("!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/")

    score = 0

    if len(pw) >= min_length:
        score += 1

    if any(ch.isdigit() for ch in pw):
        score += 1

    if any(ch.isupper() for ch in pw):
        score += 1

    if any(ch in symbols for ch in pw):
        score += 1

    if score <= 1:
        return "weak"
    elif score <= 3:
        return "medium"
    else:
        return "strong"


password = input("Enter a password: ")

print("Default check:", check_password(password))
print("Min length 12:", check_password(password, min_length=12))

"""

Exercise 3 — Receipt Builder 🧾
A real variadic API: any number of line items (*args) plus optional settings (**kwargs).

Your task: in receipt_builder.py

def build_receipt(*items, gst_percent=18, currency="Rs", **extra):
*items = any number of (name, price) tuples.
gst_percent, currency = defaults the caller can override.
**extra = anything else (e.g. customer="Asha"), printed as a footer.
Loop the items, print each line, accumulate the subtotal.
Add GST, print the grand total, then print any **extra footer fields.
Skills: *args, **kwargs, default args, the accumulate pattern (Day 4), tuple unpacking. Focus: how *args/**kwargs make one function handle calls of any shape

"""
#solution
def build_receipt(*items, gst_percent=18, currency="Rs", **extra):
    subtotal = 0

    print("===== RECEIPT =====")

    for name, price in items:
        print(f"{name}: {currency}{price:.2f}")
        subtotal += price

    gst = subtotal * gst_percent / 100
    grand_total = subtotal + gst

    print("-------------------")
    print(f"Subtotal: {currency}{subtotal:.2f}")
    print(f"GST ({gst_percent}%): {currency}{gst:.2f}")
    print(f"Grand Total: {currency}{grand_total:.2f}")

    if extra:
        print("\n--- Extra Details ---")
        for key, value in extra.items():
            print(f"{key}: {value}")


# Example calls
build_receipt(
    ("Notebook", 120),
    ("Pen", 20),
    ("Bag", 850),
    customer="Asha",
    payment="UPI"
)

print()

build_receipt(
    ("Laptop", 55000),
    ("Mouse", 1200),
    gst_percent=12,
    currency="₹",
    customer="Rahul",
    city="Lucknow"
)
