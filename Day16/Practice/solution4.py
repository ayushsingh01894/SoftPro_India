def check_password(password):
    #flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_characters:
            has_special = True

    score = 0

    if len(password) >=8:
        score += 1
    if has_upper:
        score +=1
    if has_lower:
        score +1
    if has_digit:
        score +1
    if has_special:
        score +1

    # strength

    if score == 5:
        strength = "Strong"
    elif score >=3:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"\n Score: {score} out of 5 -> {strength}")

    if strength == "Strong":
        print("Nothing is missing")
    else:
        if len(password)<8:
            print("At least 8 characters ")
        if not has_upper:
            print("at least one Uppercase letter")
        if not has_lower:
            print("at least one Lowercase letter")
        if not has_digit:
            print("At least one aor two digits must be  in strong passwords")
        if not has_special:
            print("At least one special character like @#$ etc...")

while True:

    password = input("\n Enter a password:")
    check_password(password)

    again = input("\n Check another passswords? (y/n) : ").lower().strip()

    if again !="y":
        print("Bhai password check kr liya to ab padhai start kr le")
        break