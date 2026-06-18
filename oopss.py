#class variables 

class Collage:
    collage_name = "Invertis UNiversity"

    def __init__(self, student):
        self.student = student


s1 = Collage("ayush")

print(s1.collage_name)
print(Collage.collage_name)
print(s1.student)


#inheritence 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Python Basics", "Ayush Singh")

print("Title:", b1.title)
print("Author:", b1.author)


# . Create a Mobile Class
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

m1 = Mobile("Samsung", 25000)

print("Brand:", m1.brand)
print("Price:", m1.price)

# 3. Student Class with Display Method

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)

s1 = Student("Ayush", "MCA")
s1.display()
# Medium Level
# 4. Rectangle Area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(10, 5)
print("Area =", r.area())

# Output

# Area = 50
# 5. Bank Account
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(5000)

acc.deposit(2000)
acc.withdraw(1000)

acc.show_balance()
# 6. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

c = Calculator()

print(c.add(10, 5))
print(c.subtract(10, 5))
print(c.multiply(10, 5))
# Inheritance
# 7. Person → Teacher
class Person:
    def introduce(self):
        print("I am a Person")

class Teacher(Person):
    def teach(self):
        print("I teach students")

t = Teacher()

t.introduce()
t.teach()
# 8. Vehicle → Bike
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):
    pass

b = Bike()
b.start()
9. Animal → Cat
class Animal:
    def sound(self):
        print("Animal Sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()
# Encapsulation
# 10. Private Variable
class Student:
    def __init__(self):
        self.__marks = 95

    def show_marks(self):
        print(self.__marks)

s = Student()
s.show_marks()

# Output

# 95
# Polymorphism
# 11. Same Method Different Output
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()


# Abstraction
# 12. Abstract Class Example
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())
