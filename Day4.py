#while loop 

count = 1

while count <= 5:
    print(f"Rep {count} of 5")
    count += 1

print("Done counting\n")

count = 10

while count >= 1:
    print(f"Rep {count} of 10")
    count -= 1

print("Done counting\n")

pending_order = ["ORD-101","ORD-102","ORD-103","ORD-104"]
while pending_order:
    order = pending_order.pop(0)
    print(f"Processing {order}..shipped!")
print("All order processed !.\n")


#break is used to immediately exit a loop (for or while) before it finishes normally.

#Example with while
count = 1

while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1


# print("Tiny menu - type 'quit' to leave")
# while True:
#     choice = input("Pick(status/help/quit)".strip().lower())
#     if choice == "quit":
#         print("Bye")
#         break
#     elif choice == "status":
#         print("All system up")
#     elif choice == "help":
#         print("Commands : status ,help ,quit")
#     else:
#         print(f"Unknown choice.....{choice}")

for ch in "Python":
    print(ch)


Students = ["Ayush", "Princ", "Akash"]
for Student in Students:
    print(f"Welcome {Student} !")

for i in range(1, 11):
    print(i)

#Total cart value calculator
cart = [300, 499, 88, 2000]

total = 0
for price in cart:
    total += price

print(f"Total Cart Value = {total} .")


leaderboard = ["Akash" , "Prince","Ayush"]
for rank , name in enumerate(leaderboard,start=1):
    print(f"# {rank} : {name} ")



#task : For a given list of price create a new list

prices = [300, 400, 88, 2000]
dsct_p = [price * 0.9 for price in prices]
print(dsct_p)



prices = [300, 400, 88, 2000]
dsct_p = []
for price in prices:
    discount_price = price * 0.9
    dsct_p.append(discount_price)
print(dsct_p)


#Range -- (start,end,steps)
for i in range(1,10):
    print(f"Range of {i}.")


# for i in range(1, 11):
#     print(f"7 X {i} = {7 * i}")


# for i in range(0,101,2):
#     print(f"Even numbers = {i}.")

# for i in range(1, 101, 2):
#     print(f"Even numbers = {i}.")



order = [100 , 299 ,499,1299,99]
for amount in order:
    if amount >=1000:
        print(f"We have a BIG order : Rs {amount}.. Stopping")
        break
    print(f"Checked Rs {amount}: Small Order")

#continue -- skips the round
transaction = [300,343,800,363,-300,-299,400]
income = 0
for t in transaction:
    if t < 0 :
        print(f"Skipping refunds :{t}")
        continue
    income += t
print(f"Total income : {income}")


transaction = [300, 343, 800, 363, -300, -299, 400]
income = 0
refunds = 0
for t in transaction:
    if t < 0:
        refunds += t
    else:
        income += t

print(f"Income: {income}")
print(f"Refunds: {refunds}")
print(f"Net income: {income + refunds}")


import time

correct_password = "Ayush@01894"
attempts = 0
max_attempts = 3

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    # attempts += 1
    # remaining = max_attempts - attempts

    # if remaining > 0:
    #     print(f"Wrong password! {remaining} attempts left.")

    # if attempts == max_attempts:
    #     print("Account locked for 10 seconds...")
    #     time.sleep(10)
    #     print("You can try again.")
    #     attempts = 0
    else:
        print("Wrong answer")


# correct_password = "Ayush@01894"
# while True:
#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Login Successful!")
#         break
#     else:
#         print("Wrong answer")


#Tasks

# correct_password = "Ayush@01894"
# attempt_left = 3
# while attempt_left > 0:
#     entered_password = input(f"Enter password ({attempt_left} attempts left): ")
#     if entered_password == correct_password:
#         print("Access Granted!")
#         break
#     attempt_left -= 1
#     print("Wrong Password")
# else:
#     print("Account blocked!")


#nested loops

for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

colors = ["Red","Blue"]
sizes = ["S","M","L"]
print("Generating Variants")
for color in colors:
    for size in sizes:
        sku = f"Tshirt - {color[:4].upper()} - {size}"
        print(f"{color} | {size} --> {sku}")
    print()


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: