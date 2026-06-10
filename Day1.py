print("ayush")
print("binary",0b1010)
print("octal",0o12)
print("hexadecimal",0x1A)
print("float",3.14)
print("scientific notation",1.5e2)
print("string", "Hello, World!")
print("boolean", True)
print("list", [1, 2, 3, 4, 5])
print("tuple", (1, 2, 3))
print("dictionary", {"name": "Alice", "age": 30})
print("set", {1, 2, 3})
print("NoneType", None)

#ARITHMETIC OPERATORS

operator = 5 + 3
print("addition", operator)
operator = 5 - 3
print("subtraction", operator)
operator = 5 * 3
print("multiplication", operator)
operator = 5 / 3
print("division", operator)
operator = 5 // 3
print("floor division", operator)
operator = 5 % 3
print("modulus", operator)
operator = 5 ** 3
print("exponentiation", operator)

#RELATIONAL AND LOGICAL OPERATORS

relational = 5 > 3
print("greater than", relational)
relational = 5 < 3
print("less than", relational)
relational = 5 == 3
print("equal to", relational)
relational = 5 != 3
print("not equal to", relational)
relational = 5 >= 3
print("greater than or equal to", relational)
relational = 5 <= 3
print("less than or equal to", relational)
logical = (5 > 3) and (2 < 4)
print("logical AND", logical)
logical = (5 > 3) or (2 > 4)
print("logical OR", logical)
logical = not (5 > 3)
print("logical NOT", logical)

even = 5 % 2 == 0
print("is even", even)
odd = 5 % 2 != 0
print("is odd", odd)
 
# print("Enter a number to check even or odd")   
# number = int(input("Enter a number: ")) 
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

operator_precedence = 5 + 3 * 2
print("operator precedence", operator_precedence)
operator_precedence = (5 + 3) * 2
print("operator precedence with parentheses", operator_precedence)


exponentiation = 2 ** 3
print("exponentiation", exponentiation)

""" multiline comments """  
" This is a single line comment "
" always write comment not for what its for why ? "


"Variables- that hold a value and can be used to store and manipulate data in a program"
x = 10
y = 5
sum = x + y
print("sum of x and y is", sum)

# Reassignment of variable
x = 20
print("new value of x is", x)

# Multiple assignment
a, b, c = 1, 2, 3
print( a, b, c)

# swap without using temporary variable
a = 1
b = 2 
a, b = b, a
print("after swapping a is", a, "and b is", b)

# set several at one time
x = y = z = 0
print("x:", x, "y:", y, "z:", z)

snake case = "this_is_snake_case"
camel case = "thisIsCamelCase"  
pascal case = "ThisIsPascalCase"


identifier = "valid_identifier"
# invalid identifier 
# 1variable = 10 -- is not valid because it starts with a number
# variable-name = "invalid" -- is not valid because it contains a hyphen its used in java script

_variable = "valid"
print(_variable)
variable_name = "valid"
print(variable_name)
variableName = "valid"
print(variableName)

# assigment operators
x = 10
x += 5
print(x)
x -= 5
print(x)
x *=2
print(x)
x /= 2
print(x)
x //= 3
print(x)
x **= 2
print(x)
x %= 3
print(x)

types of print function
print("Hello", "World", sep="-")  # Output: Hello-World every comma is replaced by sep
print("Hello", "World", sep=" ")  # Output: Hello World
print("Hello", "World", sep="")   # Output: HelloWorld

# Output: Hello World (without newline)
print("Hello", end=" ")  # Output: Hello World (without newline) 
print("World")  # Output: Hello World (with newline)



give me exercises for this topicSure! all which i have covered in this Day1.py
1. Write a Python program to demonstrate the use of different data types (integer, float, string, boolean, list, tuple, dictionary, set, NoneType).
2. Write a Python program to perform basic arithmetic operations (addition, subtraction, multiplication, division, floor division, modulus, exponentiation) on two numbers.
3. Write a Python program to demonstrate the use of relational and logical operators.
4. Write a Python program to check if a given number is even or odd.
5. Write a Python program to demonstrate operator precedence and the use of parentheses.
6. Write a Python program to demonstrate the use of comments and docstrings.
7. Write a Python program to demonstrate variable assignment, reassignment, and multiple assignment.
8. Write a Python program to swap the values of two variables without using a temporary variable.
9. Write a Python program to demonstrate the use of different types of print function parameters (sep and end).
10. Write a Python program to demonstrate the use of assignment operators (+=, -=, *=, /=, //=, **=, %=).
11. Write a Python program to demonstrate the use of different naming conventions (snake_case, camelCase, PascalCase) for variables and identifiers.
12. Write a Python program to demonstrate the use of valid and invalid identifiers.
13. Write a Python program to demonstrate the use of the NoneType data type and its behavior in different contexts.
14. Write a Python program to demonstrate the use of sets and their properties (e.g., uniqueness, unordered nature).
15. Write a Python program to demonstrate the use of dictionaries and their properties (e.g., key-value pairs, mutability).
16. Write a Python program to demonstrate the use of lists and their properties (e.g., ordered nature, mutability).
17. Write a Python program to demonstrate the use of tuples and their properties (e.g., ordered nature, immutability).
18. Write a Python program to demonstrate the use of boolean values and their behavior in conditional statements.
19. Write a Python program to demonstrate the use of scientific notation for representing large or small numbers.
20. Write a Python program to demonstrate the use of binary, octal, and hexadecimal number systems.
21. Write a Python program to demonstrate the use of operator precedence in complex expressions.
22. Write a Python program to demonstrate the use of logical operators (and, or, not) in conditional statements.
23. Write a Python program to demonstrate the use of the modulus operator to determine if a number is divisible by another number.
24. Write a Python program to demonstrate the use of the exponentiation operator to calculate powers of numbers.