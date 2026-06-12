age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Entry Allowed")
    else:
        print("Ticket Required")
else:
    print("Not Entry")

"""
logical operators

"""
age = 25
salary = 40000
print(age>=18 and salary>=25000)  # output - True
print(age>=18 and salary>=45000)  # output - False
print(age>=18 or salary>=20000)   # output - True
print(age>=20 or salary>=45000)  # output - True

is_weekend = False 
is_holiday = True
print(is_weekend or is_holiday) # output - True
print(False or False) # output - False


print(not True)  # output - False
print(not age>=18)  # output - False