# def build_receipt(*items, gst_percent=18, currency="Rs", **extra):
#     subtotal = 0

#     print("===== RECEIPT =====")

#     for name, price in items:
#         print(f"{name}: {currency}{price:.2f}")
#         subtotal += price

#     gst = subtotal * gst_percent / 100
#     grand_total = subtotal + gst

#     print("-------------------")
#     print(f"Subtotal: {currency}{subtotal:.2f}")
#     print(f"GST ({gst_percent}%): {currency}{gst:.2f}")
#     print(f"Grand Total: {currency}{grand_total:.2f}")

#     if extra:
#         print("\n--- Extra Details ---")
#         for key, value in extra.items():
#             print(f"{key}: {value}")


# # Example calls
# build_receipt(
#     ("Notebook", 120),
#     ("Pen", 20),
#     ("Bag", 850),
#     customer="Asha",
#     payment="UPI"
# )

# print()

# build_receipt(
#     ("Laptop", 55000),
#     ("Mouse", 1200),
#     gst_percent=12,
#     currency="₹",
#     customer="Rahul",
#     city="Lucknow"
# )

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

print(" ", add_cart_item("Apple"))
print(" ", add_cart_item("Banana"))
print(" ", add_cart_item("Bread"))

def add_cart(item,cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(" ", add_cart("Apple"))
print(" ",add_cart("Banana"))
print(" ", add_cart("Milk"))



# Local and Global 
name = "ayush singh"
def show_total():
    total = 1000
    print("Welcome :",name) #global function
    print("Total :",total)  #local function

show_total()


#function inside function inclosy function

def make_multiplier(factor):
    """Return a function that multiplies its input."""
    def multiply(n):
        return n * factor
    return multiply

triple = make_multiplier(3)
print(triple(10))

tenfold = make_multiplier(30)
print(tenfold(90))

multi = make_multiplier(4)
print(multi(8))

#args_keywords
"""
*args (extra positionals -> tuplee) *args is used to allow a function to accept a variable number of positional arguments.
**kwargs(extra keywords)  collects extra keyword arguments into a dictionary.

def introduce(title, *args):
    print("Title:", title)
    print("Names:", args)

introduce("Students", "Ayush", "Deepak", "Divyanshu")
"""
def add_numbers(*args):
    print("Args is a tuple", args)
    return sum(args)

print("Total sum : ",add_numbers(1, 2, 3, 4))
print("Total sum : ",add_numbers(1, 4))
print("Total sum : ",add_numbers())

def make_user(**kwargs):
    print("Kwargs is a dict :",kwargs)
    return kwargs

make_user(name="ayush" ,age=22,city="lucknow")
make_user(name="ayush" ,age=22,city="lucknow",contect_number=8009954066)
