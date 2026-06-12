""" what is string
A string is a sequence of characters, typically used to represent text. In programming languages,
strings are often enclosed in quotation marks (either single or double)
to differentiate them from other data types. For example, "Hello, World!" is a string. 
Strings can contain letters, numbers, symbols, and spaces. 
They are commonly used for storing and manipulating text data in various applications.

the ai job and freelance market 
ai/llm engineer
rag/search specialist  (done)
al automation freelancer  (done)
agent developer 
ai product builder
ai augmented anything 
langchain

"""

Greeting = "Hello"
Name = 'Ayush'
print(Greeting + " " + Name)
print(type(Greeting))
print(type(Name))

print("It's a sunny day")
print('he said "Hii" to everyone')

# concatenation
first = "Ayush"
last = "singh"
full = first + " " + last + " " + "is a good Engineer" 
print(full)

#Repetition
print("Haa" * 5)
print("=" * 20)

age = 25
print("Age:"+ str(age))  # converting integer to string for concatenation


#None datatype
value = None
print(value)
print(type(value)) 

#String indexing
word = "Hello" 
print(word[0])  # prints 'H'
print(word[4])  # prints 'o'
print(word[2])  # prints 'l'

print("Last chat",word[-1])
print("Last chat",word[-4])

#String slicing
word = "python"
print(word[0:3])  # prints 'pyt'
print(word[1:4])  # prints 'yth'
print(word[2:5])  # prints 'tho'
print(word[-1])   # prints 'n'
print(word[:3])   # prints 'pyt'
print(word[3:])   # prints 'hon'
print(word[-3:])   # prints 'hon'
print(word[:-2])   # prints 'pyth'

#The step
print(word[::2]) # prints 'pto'
print(word[::3]) # prints 'ph'


#reverse a string
print(word[::-1]) # prints 'nohtyp'
print(word[0:10000]) # prints 'pyhton' (slicing beyond the length of the string does not cause an error)

#escapecharacters
print("line 1 :\n line 2.")
print("Name : \t Ayush")


#triple quoted 
triple_quote = """This is a triple quoted string.
It can span multiple lines.
It is useful for docstrings and multi-line comments.
You can include both single and double quotes without escaping them.
"hello" 'world'
"""
print(triple_quote) 

#\" and \' are used to include double and single quotes in a string without ending the string.
print("He Said \"Hii\" to everyone")
print('It\'s Fine')  
print("C:\\Users\Ayush\Documents")  # using double backslashes to include a single backslash in the string
print(r"C:\Users\Ayush\Documents")  # using raw string also instead of double backslashes

#length of string
string = "Hello, World!"
print(len(string))  # prints 13
print((len("Ayush")))  # prints 5


#input user

# name = input("Enter your name: ")
# print("Nice to meet you", name)
# print("Your name has", len(name), "characters")


# Age = int(input("how old are you: "))
# print("You are", Age + 1, "years old.")
# #another way to get integer input to the user without converting it to string first
# Age = input("how old are you: ")
# print("You are", int(Age) + 1, "years old.")

# Different type of string formatting
# 1. using + operator
# name = "Ayush"      
# age = 25
# print("My name is " + name + " and I am " + str(age) + " years old.")
# # 2. using f-strings (formatted string literals)
# print(f"My name is {name} and I am {age} years old.")
# # 3. using the format() method
# print("My name is {} and I am {} years old.".format(name, age))
# # 4. using % operator
# print("My name is %s and I am %d years old." % (name,age))

#f-strings
name = "Ayush"
age = 25
location = "lucknow"
print("you are " + name + " and you are " + str(age) + " years old and you live in " + location + ".")
print(f"My name is {name}, i am {age} years old and i live in {location}.")
print(f"you are next year {age + 1} years old.")

#formatting numbers with f-strings
price = 2499.50000
print(f"Price: {price:.2f}")  # prints 'Price: 2499.50' (formats the price to 2 decimal places)
print(f"Price: {price:,.2f}")  # prints 'Price: 2,499.50' (formats the price with commas and 2 decimal places)
number = 123456789
print(f"Number: {number:,}")  # prints 'Number: 123,456,789' (formats the number with commas as thousands separators)


#String methods - built in tool for cleaninfg and manipulating strings
text = "  Ayush, Singh!  "
print(text.lower())  # prints '  ayush, singh!  ' 
print(text.upper())  # prints '  AYUSH, SINGH!  ' 
print(text.strip())  # prints 'Ayush, Singh!' 
print(text.replace("Ayush", "Hi"))  # prints '  Hi, Singh!
print(text.title())  # prints '  Ayush, Singh!  '
print(text.capitalize())  # prints '  ayush, singh!  ' 
print(text.count("a"))  # prints 1 
print(text.find("Singh"))  # prints 8 
print(text.split(","))  # prints ['  Ayush', ' Singh!  '] 
print(text.startswith("  Ayush"))  

print(text.endswith("!  ")) 

