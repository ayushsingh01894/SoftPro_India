""" personal branding means creating a unique image and reputation for yourself in the minds of others. 
It involves showcasing your skills,
values, and personality to stand out and make a positive impression. 
Personal branding can help you build credibility, attract opportunities, 
and establish yourself as an expert in your field. It is important to be authentic 
and consistent in your personal branding efforts to create a strong and memorable brand identity.
"""


is_raining = True
is_sunny = False
print(is_raining)
print(is_sunny)
print("type ==> ",type(is_raining))
print("type ==> ",type(is_sunny))

real_bool = True
fake_bool = "true" 

print("real_bool ==> ",type(real_bool))
print("fake_bool ==> ",type(fake_bool))

# #boolen usually comes from questions.
# age = 20
# is_adult = age >= 18
# print(is_adult)

# #task take age input and tell is they can vote or not
# age = int(input("Enter your age: "))
# can_vote = age >= 18    
# print(f"Can you vote? {can_vote}")

# true + true
print(True + True)  # Output: 2
print(True + False)  # Output: 1
print(False + 10)  # Output: 10
print(True * 5)  # Output: 5
print(int(True),int(False)) # Output: 1 0


# typecast to bool-truthiness
print(bool(0))  # Output: False
print(bool(1))  # Output: True
print(bool(""))
print(bool("hii"))
print(bool(None))


#comparision operator
print(5>3) #true
print(5<3)  #false
print(5>=3) #true
print(5<=3) #fasle
print(5==3) #false
print(5!=3) #true


print("apple"<"banana")  #true
print("cat" == "cat")  #true
 #comapring acrooss types
print(10=="10")  #false
print(10 == 10.0)  #true
# print(10 < "10") this give an errors 


#truthiness and falsy values
print("="*10)
print(bool(0))  # Output: false
print(bool(0.0))  # Output: false
print(bool(""))   # Output: false
print(bool([]))  # Output: false
print(bool(None))   # Output: false
print(bool({}))   # Output: false

print("="*10)
#truthiness value

print(bool(-5))  # Output: True
print(bool(1))  # Output: True
print(bool("0"))  # Output: True
print(bool("hello"))  # Output: True
print(bool("hii"))  # Output: True
print(bool(" ")) # Output: True

# Name = input("Enter your name :")
# if Name:
#     print(f"Hello {Name}")
# else:
#     print("you didn't enter your name")

# In or not (used to check condition)

print("a" in "cat")
print("a" not in "cat")


#conditional statement 
temp =  45
if temp >= 45:
    print("it's Hot!")
elif temp <= 45:
    print("its cold!")
else:
    print("nothing!")

Age = 20

if Age >=18:
    print("You can vote !")
else:
    print("Too young to vote!")

#Another example of if/elif/else conditions
marks = 72 
if marks > 90:
    grade = "A"
elif marks >=75:
    grade = "B"
elif marks >=60:
    grade = "C"
elif marks >=40:
    grade = "D"
else:
    grade ="E"
print(f"Your Marks : {grade}")
