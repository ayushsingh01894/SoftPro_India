"""
1. List

A list is an ordered, mutable collection.
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits[0] = "grape"
print(fruits)

Output:
['grape', 'banana', 'mango', 'orange']

Use lists when:
Order matters.
Items may change.
Duplicates are allowed.
2. Tuple
A tuple is an ordered, immutable collection.
point = (10, 20)
print(point[0])

Output:
10

Trying to modify it:
point[0] = 15
Produces:
TypeError: 'tuple' object does not support item assignment
Use tuples when:
Data should not change.
You want a fixed collection of values.


3. Dictionary
A dictionary stores key-value pairs.
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}
print(student["name"])

Output:
Rahul
Adding a new item:
student["city"] = "Lucknow"
Use dictionaries when:
You need fast lookup by key.
Data has named attributes.


4. Set
A set stores unique values.
numbers = {1, 2, 3, 2, 1}
print(numbers)

Output:
{1, 2, 3}

Duplicates are removed automatically.
Adding elements:
numbers.add(4)
Use sets when:
You need unique items.
You perform union, intersection, or difference operations.

Example:
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # Intersection
print(a | b)  # Union

Output:

{3}
{1, 2, 3, 4, 5}


Quick Memory Trick
List → "Shopping list" → ordered and editable.
Tuple → "Coordinates (x, y)" → ordered and fixed.
Dictionary → "Word dictionary" → key → value.
Set → "Unique collection" → no duplicates

"""

"""
Creating Lists
numbers = [1, 2, 3, 4]
empty = []
mixed = [1, "hello", 3.14, True]
Accessing Elements
numbers = [10, 20, 30, 40]

print(numbers[0])    # 10
print(numbers[-1])   # 40

Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]
print(numbers[::-1])  # Reverse

Adding Elements
append()
lst = [1, 2]
lst.append(3)

print(lst)  # [1, 2, 3]
extend()
lst = [1, 2]
lst.extend([3, 4])

print(lst)  # [1, 2, 3, 4]
insert()
lst = [1, 3]
lst.insert(1, 2)

print(lst)  # [1, 2, 3]

Removing Elements
remove()
lst = [1, 2, 3]
lst.remove(2)
print(lst)  # [1, 3]

pop()
lst = [1, 2, 3]
item = lst.pop()
print(item)  # 3
print(lst)   # [1, 2]
lst.pop(0)

del
lst = [1, 2, 3]
del lst[1]
print(lst)  # [1, 3]

clear()
lst = [1, 2, 3]
lst.clear()

print(lst)  # []

Searching
index()
lst = [10, 20, 30]
print(lst.index(20))
Output:1

count()
lst = [1, 2, 2, 3]
print(lst.count(2))

Output:2

in Operator
lst = [1, 2, 3]
print(2 in lst)
print(5 in lst)

Output:
True
False

Sorting
sort()
lst = [5, 2, 8, 1]
lst.sort()
print(lst)

Output:
[1, 2, 5, 8]

Descending:
lst.sort(reverse=True)

sorted()
lst = [5, 2, 8]
new_list = sorted(lst)
print(new_list)

Reversing
reverse()
lst = [1, 2, 3]
lst.reverse()

print(lst)

Output:
[3, 2, 1]

Copying
copy()
lst1 = [1, 2, 3]
lst2 = lst1.copy()
print(lst2)

List Slice Copy
lst2 = lst1[:]
Joining Lists
a = [1, 2]
b = [3, 4]
c = a + b
print(c)

Output:
[1, 2, 3, 4]

Repeating Lists
lst = [1, 2]
print(lst * 3)

Output:
[1, 2, 1, 2, 1, 2]

Length
lst = [1, 2, 3]
print(len(lst))

Output:
3
Min, Max, Sum
nums = [10, 20, 30]
print(min(nums))
print(max(nums))
print(sum(nums))

Output:
10
30
60

Iterating
lst = [10, 20, 30]
for item in lst:
    print(item)

With index:
for i, value in enumerate(lst):
    print(i, value)

List Comprehension
squares = [x*x for x in range(5)]
print(squares)

Output:
[0, 1, 4, 9, 16]

With condition
evens = [x for x in range(10) if x % 2 == 0]
Useful Built-in Functions
lst = [3, 1, 4]

len(lst)
sum(lst)
min(lst)
max(lst)
sorted(lst)
any(lst)
all(lst)
Complete List Methods
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()

"""

"""
Tuple in Python

A tuple is an ordered, immutable collection.
t = (10, 20, 30)
Creating Tuples
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (1, "hello", 3.14)

empty = ()
single = (10,)   # Comma is required
Without the comma:

x = (10)
print(type(x))   # int


Accessing Elements
t = (10, 20, 30, 40)
print(t[0])    # 10
print(t[-1])   # 40

Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[2:])    # (30, 40, 50)
print(t[::-1])  # Reverse

Tuple Packing
t = 10, 20, 30
print(t)

Output:
(10, 20, 30)

Tuple Unpacking
t = (10, 20, 30)
a, b, c = t
print(a)
print(b)
print(c)

Output:
10
20
30

Extended Unpacking
t = (1, 2, 3, 4, 5)
a, *b, c = t

print(a)
print(b)
print(c)

Output:
1
[2, 3, 4]
5

Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2

print(t3)

Output:
(1, 2, 3, 4)

Repetition
t = (1, 2)
print(t * 3)
Output:

(1, 2, 1, 2, 1, 2)

Membership Operators
t = (10, 20, 30)

print(20 in t)
print(50 not in t)

Output:

True
True


Iteration
t = (10, 20, 30)
for item in t:
    print(item)

With index:

for i, value in enumerate(t):
    print(i, value)

Built-in Functions
t = (10, 20, 30, 40)

print(len(t))
print(min(t))
print(max(t))
print(sum(t))

Output:

4
10
40
100
Tuple Methods

Tuples have only 2 methods because they are immutable.

count()
t = (1, 2, 2, 3)
print(t.count(2))

Output:

2
index()
t = (10, 20, 30)

print(t.index(20))

Output:

1
Converting Between List and Tuple
Tuple → List
t = (1, 2, 3)

lst = list(t)

print(lst)
List → Tuple
lst = [1, 2, 3]

t = tuple(lst)

print(t)
Immutability
t = (10, 20, 30)

t[0] = 100

Error:

TypeError: 'tuple' object does not support item assignment
Nested Tuples
t = ((1, 2), (3, 4))

print(t[0])
print(t[1][1])

Output:

(1, 2)
4
Tuple vs List
Feature	Tuple	List
Ordered	Yes	Yes
Mutable	No	Yes
Duplicates	Yes	Yes
Syntax	()	[]
Methods	2	11+
Faster	Yes	Slightly slower
All Tuple Operations at a Glance
t = (1, 2, 3)

t[0]          # Access
t[-1]         # Negative index
t[1:3]        # Slice
len(t)        # Length
min(t)        # Minimum
max(t)        # Maximum
sum(t)        # Sum
1 in t        # Membership
t + (4, 5)    # Concatenation
t * 2         # Repetition
t.count(2)    # Count occurrences
t.index(3)    # Find index

"""

"""
A dictionary (dict) in Python stores data as key-value pairs.

Creating a Dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print(student)

Output:
{'name': 'Rahul', 'age': 20, 'course': 'Python'}

Common Dictionary Operations
1. Access Values

student = {"name": "Rahul", "age": 20}
print(student["name"])
print(student.get("age"))

Output:
Rahul
20

2. Add New Key-Value Pair
student["city"] = "Lucknow"
print(student)

Output:
{'name': 'Rahul', 'age': 20, 'city': 'Lucknow'}

3. Update Value
student["age"] = 21
print(student)
Output:

{'name': 'Rahul', 'age': 21}

4. Remove Items
pop()
student = {"name": "Rahul", "age": 20}
student.pop("age")
print(student)

Output:
{'name': 'Rahul'}

del
del student["name"]

clear()
student.clear()
print(student)

Output:
{}

Dictionary Methods
keys()
student = {"name": "Rahul", "age": 20}
print(student.keys())

Output:

dict_keys(['name', 'age'])

values()
print(student.values())

Output:
dict_values(['Rahul', 20])

items()
print(student.items())

Output:

dict_items([('name', 'Rahul'), ('age', 20)])

update()
student.update({"city": "Lucknow"})
print(student)

Output:

{'name': 'Rahul', 'age': 20, 'city': 'Lucknow'}

setdefault()
student.setdefault("marks", 90)

print(student)

Output:
{'name': 'Rahul', 'age': 20, 'marks': 90}

popitem()
Removes the last inserted item.

student = {"name": "Rahul", "age": 20}
student.popitem()
print(student)

Output:

{'name': 'Rahul'}

copy()
new_student = student.copy()

fromkeys()
keys = ["name", "age", "city"]

d = dict.fromkeys(keys, "N/A")
print(d)

Output:

{'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}

Loop Through Dictionary
Loop Keys
for key in student:
    print(key)
Loop Values
for value in student.values():
    print(value)
Loop Key-Value Pairs
for key, value in student.items():
    print(key, ":", value)

Output:

name : Rahul
age : 20

Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}

print(squares)

Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Useful Interview Points

Dictionaries are mutable.
Keys must be unique.
Keys must be immutable types (string, int, tuple, etc.).
Values can be of any type.
Average time complexity for lookup, insert, delete: O(1).
Python dictionaries preserve insertion order (Python 3.7+).
Example
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 95
}

for k, v in student.items():
    print(f"{k} -> {v}")

Output:

name -> Rahul
age -> 20
marks -> 95

"""


"""
Python set — Complete Overview

A set is an unordered collection of unique elements.

fruits = {"apple", "banana", "mango"}
print(fruits)
Characteristics
No duplicate values
Unordered (no indexing)
Mutable (can add/remove items)
Fast membership testing (in)
Creating Sets
Using curly braces
numbers = {1, 2, 3, 4}
print(numbers)
Using set()
numbers = set([1, 2, 3, 4])
print(numbers)
Empty Set
s = set()      # Correct
print(type(s))

Not:

s = {}        
# Dictionary, not a set
Removing Duplicates
nums = {1, 2, 2, 3, 3, 4}
print(nums)

Output:

{1, 2, 3, 4}
Adding Elements
add()
fruits = {"apple", "banana"}
fruits.add("mango")

print(fruits)
update()

Add multiple items:

fruits = {"apple", "banana"}

fruits.update(["mango", "orange"])

print(fruits)
Removing Elements
remove()
fruits = {"apple", "banana"}

fruits.remove("apple")

print(fruits)

Error if item doesn't exist:

fruits.remove("grapes")   # KeyError
discard()

No error if item doesn't exist.

fruits.discard("grapes")
pop()

Removes a random element.

fruits = {"apple", "banana", "mango"}

item = fruits.pop()

print(item)
print(fruits)
clear()
fruits.clear()

print(fruits)

Output:

set()
Membership Testing
fruits = {"apple", "banana"}

print("apple" in fruits)
print("mango" in fruits)

Output:

True
False
Iterating Through a Set
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)
Set Operations
Union (|)
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

Output:

{1, 2, 3, 4, 5}

or

print(a.union(b))
Intersection (&)

Common elements:

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)

Output:

{2, 3}

or

print(a.intersection(b))
Difference (-)
a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)

Output:

{1}
Symmetric Difference (^)

Elements present in only one set.

a = {1, 2, 3}
b = {2, 3, 4}

print(a ^ b)

Output:

{1, 4}
Useful Methods
Copy
a = {1, 2, 3}

b = a.copy()

print(b)
Length
s = {1, 2, 3, 4}

print(len(s))
Maximum and Minimum
s = {10, 20, 30}

print(max(s))
print(min(s))
Set Comprehension
s = {x*x for x in range(5)}

print(s)

Output:

{0, 1, 4, 9, 16}
Frozen Set (Immutable Set)
fs = frozenset([1, 2, 3])

print(fs)

Cannot modify:

fs.add(4)   # Error
Interview Questions
Remove Duplicates from a List
nums = [1, 2, 2, 3, 3, 4]

unique = list(set(nums))

print(unique)
Find Common Elements
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = set(a) & set(b)

print(common)
Check Subset
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))

Output:

True
Check Superset
print(b.issuperset(a))

Output:

True
Quick Reference
Method	Description
add()	Add one item
update()	Add multiple items
remove()	Remove item (error if absent)
discard()	Remove item (no error)
pop()	Remove random item
clear()	Remove all items
union()	Combine sets
intersection()	Common elements
difference()	Elements in first set only
symmetric_difference()	Non-common elements
issubset()	Check subset
issuperset()	Check superset
copy()	Copy set
len()	Number of elements

A set is most commonly used for removing duplicates, membership checks, and mathematical set operations like union and intersection.



"""