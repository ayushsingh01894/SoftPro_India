balance = 0
transactions = []

def get_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount > 0:
                return amount
            else:
                print("Amount must be greater then 0")
        except ValueError:
            print("Enter valid number")

def deposit():
    global balance
    amount = get_amount("Enter deposit amount : ")
    balance += amount
    transactions.append(("Deposit" , amount ,balance))
    print(f"Deposit successfully")
    print(f"balance: {balance}")


def withdraw():
    global balance
    amount = get_amount("Enter withdrawal Amount :")

    if amount > balance:
        print("insufficient balance")
    else:
        balance -= amount
        transactions.append(("Withdraw", amount , balance))
        print(f"Withdraw successfully")
        print(f"Balance : {balance}")


def Mini_statement():
    if not transactions:
        print("No transaction")
        return
    print("\nMini statements")
    for t in transactions:
        print(f"{t[0]}  {t[1]}  Balance {t[2]}")
    print(f"\nCurrent Balance: {balance}")
    
while True:
    print("\n1. Deposit ")
    print("2. Withdraw ")
    print("3. Mini statements")
    print("4. Exit ")

    Choice = input("Enter choice : ")
    if Choice == "1":
        deposit()
    elif Choice == "2":
        withdraw()
    elif Choice == "3":
        Mini_statement()
    elif Choice == "4":
        print("Thankk youu broh ")
        break
    else:
        print("Invalid choice")