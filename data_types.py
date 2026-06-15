cart =["milk","bread","banana"]
print("Cart :",cart)
print("First item of cart",cart[0])
print("Lastt item :" ,cart[-1])
print("Length :", len(cart))
print("Slice :",cart[0:2])
print("Milk in cart :", "milk" in cart)

cart[0] = "coffee"
print(cart)
cart.append("rice")
cart.insert(0,"tea")

shopping_list = ["Banana","oranges"]
cart.extend(shopping_list)
print(cart)

demo =[1,2]
demo.append([3,4])
print("demo after append :",demo)

demo =[1,2,3]
demo.extend([3,4,5])
print("demo after extends :",demo)

removed_cart =cart.pop()
print(cart)
print(removed_cart)

cart.remove("rice")
print("removed_cart_name :",cart)


lst = [1, 2, 3]   
del lst[1]
print(lst)  


# Dictionary 
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python",
    "Marks":[10,20,30,40]
}

print(student)
print(student.get("age"))
#adding new data kay and values
student["city"]="Lucknow"
print(student)
#Update Value
student["age"] = 21
print(student)
print("Name :",student["name"])
print("How many item are there :",len(student))
print("'Age' in student:","Age" in student)
student.pop("age")
print(student)
del student["name"]
print(student)

print(student.keys())
print(student.values())
print(student.items())

student.update({"city": "Mau"})
print(student)

student.popitem()
print(student)

removed_items = student.pop("Marks")
print(removed_items)
 
 #tuples 

point = (3,4)
print("Point  " ,point)
print("Point  " ,point[0])
print("Point  " ,len(point))


person = ("Ayush",34,"Ai consultent")
name , age , job = person
print(f"Name : {name} , Age : {age}, job : {job}")
name , *b = person
print(b)


# Sets 

tags = {"python","Ai","python","ml"}
print(tags)
print("ai" in tags)
tags.add("reg")
tags.add("ai")
print(tags)
tags.discard("ml")
print(tags)

empty = set()  # use to create empty sets by using set keywords 
#use sets to dedup any list used to remove duplicates
sigups = ["Aush@gmail.com","Ayyush@gmail.com","Ah@gmail.com","Aush@gmail.com"]
unique_singup = set(sigups)
print(unique_singup)

#set Algebra
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  #marge
print(a & b)  #comman 
print(a - b)  #difference
print(a ^ b)  #symentric diff