#question 1

def to_hms(total_seconds):
    hours = total_seconds // 3600
    leftover = total_seconds % 3600

    minutes = leftover // 60
    seconds = leftover % 60

    return (hours, minutes, seconds)

print(to_hms(3661))
print(to_hms(59))



#question 2  BMI calculators 

def bmi(weight_kg, height_m):
    height_squared = height_m ** 2
    value = weight_kg / (height_squared)
    
    return round(value, 1)

print(bmi(72, 1.75))
print(bmi(50, 1.60))

#question 3

def initials(full_name):
    words = full_name.split()
    result = ""

    for word in words:
        result += word[0].upper() + "."
    return result

print(initials("asha ravi rao")) 
print(initials("Sundar Pichai"))

#question 4 

def is_palindrome(test):
    cleaned_version = test.lower().replace(" ","")
    result = test[::-1]

    return result

print(is_palindrome("Race car"))
print(is_palindrome("hello"))


#question 5
def clean_title(messy):
    words = messy.split()
    cleaned_words = []

    for word in words:
        cleaned_words.append(word.capitalize())

    return " ".join(cleaned_words)

print(clean_title("  hELLo    wORLD  "))
print(clean_title("the  TODO   list"))  

#question 6 


def grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

print(grade(95))    # A
print(grade(72))    # C
print(grade(150))

#QUESTION 7

def is_leap(year):
    return  (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2024))
print(is_leap(1900))
print(is_leap(2000))


#question 8

def digit_sum(n):
    if n == 0:
        return (0, 1)

    total = 0
    count = 0

    while n > 0:
        total += n % 10
        n = n // 10
        count += 1

    return (total, count)

print(digit_sum(4096))
print(digit_sum(0))


#question 9

def triangle(n):
    for r in range(1, n + 1):
        line = ""
        for j in range(r):
            line += "* "
        print(line.rstrip())
triangle(4)

#question 10
def fibonacci(count):
    a , b = 0 ,1 
    seq =[]
    for count in range(count):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fibonacci(10)) 
print(fibonacci(1))


#question 11

def convert(temp ,to="C"):
    if to == "F":
        return round(temp * 9 / 5 + 32, 2)
    elif to == "C":
        return round((temp - 32) * 5 / 9, 2)
    else:
        return None

print(convert(100, to="F"))
print(convert(98.6))


#question 12 

def stats(*numbers):
    if not numbers:
        return None
    
    total = 0
    smallest = numbers[0]
    largest = numbers[0]

    # if num in numbers:
    #     total += num
    #     if num < smallest:
    #         smallest = num
    #     if num > largest:
    #         largest = num
    
    avg = total / len(numbers)
    return {"min": smallest, "max": largest, "avg": avg}

print(stats(4,8,2,6))
print(stats())

#question 13

def word_freq(sentence):
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def most_common(sentence):
    counts = word_freq(sentence)
    return max(counts.items())

print(word_freq("the cat the dog the")) 
print(most_common("the cat the dog the"))

#question 14

def compare(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)

    common = set_a & set_b
    only_a = set_a - set_b
    combined = set_a | set_b

    return sorted(list(common)), sorted(list(only_a)), sorted(list(combined))

print(compare([1, 2, 3, 4], [3, 4, 5]))

#question 15 
def averages(gradebook):
    result = {}
    for name, marks in gradebook.items():  result[name] = round(sum(marks)/len(marks), 2)
    return result

def topper(gradebook):
    return max(gradebook.items())


book = {"Asha": [88, 92, 79], "Ravi": [70, 65, 80], "Meena": [95, 99, 91]}
print(averages(book))
print(topper(book))


