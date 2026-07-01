users = {"aditi": "pass123", "rahul": "hunter2"}

attempt = {}
locked = set()

while True:
    while True:
        username = input("Username: ").strip()
        if username == "":
            print("Username cannot be empty.")
        else:
            break
    
    while True:
        password = input("Password: ").strip()
        if password == "":
            print("Password cannot be emoty")
        else:
            break
    
    if username in locked:
        print("Account Locked")
        continue

    if username not in users:
        print("No such user")
        continue

    if password == users[username]:
        print("Login Successsfully")
        break

    attempt[username] = attempt.get(username , 0) + 1

    if attempt[username] >=3:
        locked.add(username)
        print("Account locked!")
    else:
        left = 3 - attempt[username]
        print(f"Wrong password . left attempts: {left}")