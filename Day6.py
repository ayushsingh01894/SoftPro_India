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

let name = "Ayush";

function showName() {
    console.log(name);
}

showName();      // Ayush
console.log(name); // Ayush
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
# local function
def greet():
    message = "Hello"
    print(message)  # // Accessible

greet()

# print(message)  #not accessible from outside of the loop 

name = "ayush singh"
def show():
    print(name)  # // Accessible if variable declare outside of the function block
show()

# GLobal function

name = "ayush singh"
def show():
    print(name)  # // Accessible if variable declare outside of the function block
show()

#default value

def add_cart_item(item,cart=[]):
    cart.append(item)
    return cart

print(" ", add_cart_item ,("Apple"))
print(" ", add_cart_item ,("Banana"))
print(" ", add_cart_item ,("Bread"))


# def add_cart(item,cart=None):
