import random

current_otp = None
attempts_left = 0

while True:
    print("\n1. Send OTP")
    print("2. Enter OTP")
    print("3. Exit")

    choice = input("Choice: ").strip()

    if choice == "1":
        current_otp = random.randint(100000, 999999)
        attempts_left = 3
        print(f"Your OTP is {current_otp}")

    elif choice == "2":

        if current_otp is None:
            print("No OTP sent yet.")
            continue

        if attempts_left == 0:
            print("OTP expired.")
            continue

        entered = input("Enter OTP: ").strip()

        if not (entered.isdigit() and len(entered) == 6):
            print("Enter a valid 6-digit code.")
            continue

        if entered == str(current_otp):
            print("Verified!")
            current_otp = None
            attempts_left = 0
        else:
            attempts_left -= 1

            if attempts_left == 0:
                print("OTP expired.")
                current_otp = None
            else:
                print(f"Wrong OTP. Attempts left: {attempts_left}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")