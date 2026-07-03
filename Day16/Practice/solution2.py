"""

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



"""

import random

class OTPEngine:
    def __init__(self, length=6,max_attempts=3):
        self.length = length
        self.max_attempts = max_attempts
        self.otp = None
        self.attempts_left = 0

    def send(self):
        low  = 10 ** (self.length - 1)
        high = 10 ** self.length - 1
        self.otp = random.randint(low,high)

        self.attempts_left = self.max_attempts

        print(f"SMS : Your OTP is {self.otp}")

        return self.otp
    
    def verify(self ,entered):
        if self.otp is None:
            return "NO OTP"

        if self.attempts_left <= 0:
            return "Expired"

        if entered == self.otp:
            self.otp = None
            return "ok"

        self.attempts_left -= 1

        if self.attempts_left <=0:
            return "Expired"
        
            return "Wrong"

if __name__ == "__main__":
    engine = OTPEngine(length=6, max_attempts=3)

    real = engine.send()               # the fake gateway shows us the code
    print("verify(000000)  ->", engine.verify(0))       # wrong
    print("verify(guess)   ->", engine.verify(real - 1))  # wrong again
    print(f"verify({real}) ->", engine.verify(real))    # correct -> OK
    print("verify(again)   ->", engine.verify(real))    # OTP already consumed

    print("\n-- resend, then burn all attempts --")
    real = engine.send()
    for guess in (1, 2, 3):            # 3 wrong tries exhausts the budget
        print(f"verify({guess}) ->", engine.verify(guess))
    print(f"verify({real}) ->", engine.verify(real)) 