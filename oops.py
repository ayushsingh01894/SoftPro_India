"""
Class and Object in Python
Python is an Object-Oriented Programming (OOP) language. The two basic concepts are:
1. Class
A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that objects will have.
Syntax:

class Student:
    pass


2. Object
An object is an instance of a class. It is created from the class blueprint.

Think of a Class as a Car Blueprint and an Object as an actual Car built from that blueprint.
Class	Object
Blueprint of a car	Actual car
Defines properties	Contains actual values
Created once	Can create many objects

"""

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed


rex = Dog("Rex","Labrador")
kallu = Dog("Kallu","Desi")

print(rex.name,rex.breed)
print(kallu.name,kallu.breed)

# kallu.name = "Dogesh"

class Student:
    def __init__(self,name,rollno,email):
        self.name = name
        self.rollno = rollno
        self.email = email

    def display(self):
        print("Name:", self.name)
        print("RollNo", self.rollno)
        print("Email:", self.email)


s1 = Student("Ayush", 20, "ayush.singh01894@gmail.com")
print(s1.name,s1.rollno,s1.email)
s1.display()

class BankAccount:
    bank_name = "SBI"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance
        

ayush = BankAccount("Ayush", 1000)
prince = BankAccount("Prince")

print(ayush.bank_name)
print(ayush.deposit(500))
print(ayush.bank_name)
print("Remaining balance :",ayush.withdraw(400))
print("Remaining balance :",ayush.withdraw(400))
print("Remaining balance :",ayush.withdraw(400))
print(ayush.withdraw(400))
print(prince.deposit(200))

#inheritence 

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "..."
    
class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meoww"

rex = Dog("Rex")
print(rex.speak())
luna = Cat("Rex")
print(luna.speak())
mystery = Animal("Mystery")
print(mystery.speak())