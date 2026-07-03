"""
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

"""

class LoginSystem:
    def __init__(self,users,max_attempts =3):
        self.users = users
        self.max_attempts = max_attempts
        self.failed = {}
        self.locked = set()

    def login(self,username,password):
        if username in self.locked:
            return 'Locked'
        if username not in self.users:
            return 'No_users'
        if self.users[username] == password:
            self.failed[username] = 0
            return 'ok'
        self.failed[username] = self.failed.get(username,0) + 1
        if self.failed[username] >= self.max_attempts:
            self.locked.add(username)
            return "Locked"
        return "Wrong"

users = {
    "aditi": "pass123", 
    "rahul": "hunter2"
}

system = LoginSystem(users)

while True:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    result = system.login(username, password)

    if result == "ok":
        print("Login Successfully!")
        break

    elif result == "Wrong":
        left = system.max_attempts - system.failed[username]
        print(f"Wrong password. Attempts left: {left}")

    elif result == "Locked":
        print("Account Locked!")

    elif result == "No_users":
        print("No such user.")
