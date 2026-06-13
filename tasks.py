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
        print(i)