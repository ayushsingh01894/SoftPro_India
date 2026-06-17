# lembda funtion - throwawy functions you write inline 
# syntex lambda arguments: expression

def squaee(n):
    return n*n
    
# end def
square_lembda = lambda n: n*n
print(square_lembda(10))
print(square_lembda(10))


add = lambda a,b: a+b
print(add(2,6))

num = [1,3,4,2,4,6]
#map : are used to apply a function to every items.
double = list(map(lambda n: n*2, num))
print(double)

#filter 
evens = list(filter(lambda n: n%2==0,num))
print(evens)

# #Reduce function
# sums = list(reduce(lambda n: n+1,num))
# print(sums)


#modules 

import math

print(math.pi)
print(math.sqrt(144))
print(math.floor(4.3))
print(math.ceil(4.3))

from random import randint,choice,seed 
print(randint(1,4))
print(choice(["Rock","paper","scissor"]))

import datetime as dt
today = dt.date.today()
print(today)
print(type(today))
print(today.year)
print(today.month)
print(today.day)
new_year = dt.date(today.year,11,18)
my_bday = dt.date(2004,11,18)
print(my_bday)
print(new_year)
print("Days to new year:", (new_year - today).days)
