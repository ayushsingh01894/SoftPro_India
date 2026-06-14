"""

Problem solving and lOgic building in python 
1. understand the problems  (input and whats going on it) input and expected output , write rules what should you can do and how ?
2. example by hand 
3. Plan
4. code 
5. test

write a plain english code how that work like data flows (pseudocode)

input like 1 to 20 numbers- expected output if any number divisible by 3 and 5 like 3,6,5,10 = are fizzbuzz
another condition if only divisible by 3 show fizz
another condition if only divisible by 5 show buzz like instead of 5 print buzz
else print normal numbers 

steps to do fizzbuzz solution
step 1. print number using for in given range
step 2. check condition divisible by 3 and 5 and reminder 0 means fizzbuzz
step 3. check another condition if only divisible by 3 means fizz
step 4. check another condition if only divisible by 5 means buzz
step 5. print variable numbers 

code. 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


Git --- Working area -(git add)-- staging area -(git commint -m "Messages")- Repository
for check we use (Git Status)

git some imp...

git --version for checking version
After download only ones u need to do that configuration and add with github account.
git config --global user.name "Ayush Singh"
git config --global user.email "your_email@example.com"

check:
git config --list

git init = for initialize 
git add "file_name"
git add . = for all info..
git status (for check status)
git commit -m "Initial commit" (first commit)
git remote add origin https://github.com/USERNAME/my-first-project.git  (for connect to repo..)
git remote -v (check)
git branch -M main
git push -u origin main (push your data into git repository)

git clone URL
git pull
git log
git status
git remote -v

@Daily working commands
git status
git add .
git commit -m "Updated project"
git push


"""  

# Python Function
"""
Function ek reusable block of code hota hai jo kisi specific task ko perform karta hai. Ek baar function bana lo, phir use baar-baar call kar sakte ho.

Syntax:
def greet():
    print("Hello!")

greet()

"""

# Docstring -- one line description 

def greet():
    """Print some info..."""
    print("Hello broh , How Are You...")
#calling funtion... by using funtion name.
greet()
print(greet())  #output - none
print(greet.__doc__) # use to show docstring like """Print some info..."""...

"""
default Parameters aand Agruments

"""

def greet(name="Friend"):  #Give by default parameter...  
    print("Hello", name)
#Calling..
greet()
greet("Ayush") #Passing Arguments at a calling time....

greet("ben")
#Argument can be expressions 
raw = "   ayush   "
greet(raw.strip().title())


# Multiple parameters 
def book_ticket(name,seat,price):
    """print a booking line"""
    print(f"{name}-->Seat : {seat} (Rs {price}).")

book_ticket("Ayush","30",10000)

order = [101,102,103]
def confirm_order(order_id):
    print(f"Order #{order_id} confirment.out for Delivery")

for i in order:
    confirm_order(i)


# Funtion with return addition 
def addition(a,b):
    return a+b
total = addition(4,5)
print(f"Totol value -- {total}")

#funtion with two return vlaue 
def safe_divide(a,b):
    if b == 0:
        return "Cannot divide by 0"
    return a/b

print(safe_divide(1,0))
print(safe_divide(0,1))

#Funtion can also return multiple values
#Python puts then in a tuple

def min_max_avg(numbers):
    return min(numbers), max(numbers),sum(numbers)/len(numbers)

numbers = [65,32,76,90,54]
print(min_max_avg(numbers))
#Spread the tuple values into diff variables 
Low , High , Avg = min_max_avg(numbers)
print(f"Lowest : {Low}, Highest : {High} ,Average : {Avg}")

#Default 
def greet(name,greeting ="Hii"):
    print(f"{greeting} , {name}")

greet("Ayush")
greet("Ayush","Welcome")


# Keyword Arguments

def book_ticket(name ,seat ,price):
    print(f"{name}--> seat {seat} (Rs {price})")

book_ticket("Ayush","56LB",5600)
book_ticket(name="Ayush",price=5600,seat="56LB")
book_ticket("Ayush",price=5600,seat="56LB")


"""
Scope function.... 

A variable declared inside a function is only available within that function.

# Example (JavaScript)
function greet() {
    let message = "Hello";
    console.log(message); // Accessible
}

greet();
console.log(message); // Error: message is not defined

Here, message has function/local scope. It exists only inside greet().

"""
"""
Global Scope

A variable declared outside all functions can usually be accessed from anywhere in the program.

let name = "Alice";

function showName() {
    console.log(name);
}

showName();      // Alice
console.log(name); // Alice
Python Example
def greet():
    message = "Hello"
    print(message)

greet()          # Hello
print(message)   # NameErro

"""

"""
Types of Scope (common in many languages)
Global Scope – accessible throughout the program.
Function/Local Scope – accessible only inside the function.
Block Scope – accessible only inside a block ({}), in languages that support it.

"""