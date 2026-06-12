import random

roll = random.randint(1, 6)  #randint is used for random integer numbers 
print(roll)

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
print(computer)

#By using normally
coins_flips = random.choice(["Heads", "Tails"])
print(coins_flips)


#By using bool method 
coin = random.choice([True, False])
if coin:
    print("Heads")
else:
    print("Tails")