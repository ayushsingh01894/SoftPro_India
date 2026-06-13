name = "  Aarav  "
clean = name.strip()
print(name.upper())
print(clean)
raw = "   pRiYa  "
clean_name = raw.strip().capitalize()
print(f"Welcome, {clean_name}!")
phone = "9876543210"
print(phone.find("5"))

name = "  Aarav  "
print(name.strip().upper())

pnr = "IRCTC2024"
code = pnr[5:9]
print(code)

marks = 70
attendance = 60

result = marks >= 40 and attendance >= 75
print(result)

# age = 20
# if age = 18:
#     print("Adult")


# 1. Truthy aur Falsy ka matlab
# Python mein kuch values condition check karte waqt  True aur False ki tarah behave karti hain. Jo values True ki tarah behave karti hain unhe Truthy kehte hain aur jo False ki tarah behave karti hain unhe Falsy kehte hain.

# 2.   0 Falsy hai kyunki Python zero ko False maanta hai.
# "" (empty string) Falsy hai kyunki isme koi character nahi hota.
# "0" Truthy hai kyunki ye empty string nahi hai. Isme ek character (0) maujood hai.

# # 3. Jab name ek string ho, to if name: check karta hai ki string khaali hai ya nahi. Agar string mein koi text hai to condition True hogi, aur agar string khaali ("") hai to condition False hogi. Yaani ye dekhne ka ek short tarika hai ki name mein koi value hai ya nahi.

# Python is expression ko operator precedence ke hisab se evaluate karta hai. and ki precedence or se zyada hoti hai, isliye pehle True and False evaluate hoga, jiska result False aata hai. Uske baad expression False or False ban jata hai, jiska result bhi False hai. Isliye result = False hoga.

# Agar hum chahte hain ki or pehle evaluate ho, to parentheses lagayenge:

# result = (False or True) and False

# Yahan pehle False or True evaluate hoga aur result True aayega. Phir True and False evaluate hoga, jiska result False hai. Isliye final result phir bhi False hi rahega.
x = 7
if x > 10:
    print("big")
elif x > 5:
    print("medium")
elif x > 3:
    print("small")
else:
    print("tiny")


age = 20
has_id = False
print(age >= 18 and has_id)

days_late = 9

if days_late == 0:
    fine = 0
elif days_late <= 7:
    fine = days_late * 2
else:
    fine = days_late * 5

print("Fine: Rs", fine)


attendance = 82
cgpa = 8.5
fee_paid = True

if attendance >= 75 and cgpa >= 8.0 and fee_paid:
    print("Scholarship: Yes")
else:
    print("Scholarship: No")

marks = 72

if marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F")