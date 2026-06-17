Problem 01 - Seconds to H:M:S   (Day 1: numbers & operators)   [STUB]

Given a whole number of seconds, break it into hours, minutes and seconds.
Example: 3661 seconds  ->  (1, 1, 1)   i.e. 1 hour, 1 minute, 1 second.

Skills: integer division //, modulo %, returning a tuple.

Run:
    python q01_seconds_to_hms.py
"""

def to_hms(total_seconds):
    """Return (hours, minutes, seconds) for the given total_seconds."""
    # TODO: hours = how many whole 3600s fit in total_seconds  (use //)
    # TODO: take what's left over after the hours          (use %)
    # TODO: from the leftover, minutes = leftover // 60, seconds = leftover % 60
    # TODO: return (hours, minutes, seconds)
    pass


if __name__ == "__main__":
    print(to_hms(3661))    # expected: (1, 1, 1)
    print(to_hms(59))      # expected: (0, 0, 59)

"""
Problem 02 - BMI Calculator   (Day 1: arithmetic & exponent)   [STUB]

BMI = weight (kg) / height (m) squared.  Round to 1 decimal place.
Example: 72 kg, 1.75 m  ->  23.5

Skills: division, the exponent operator **, round().

Run:
    python q02_bmi_calculator.py
"""

def bmi(weight_kg, height_m):
    """Return the Body Mass Index, rounded to 1 decimal place."""
    # TODO: height squared is  height_m ** 2
    # TODO: bmi value = weight_kg / (height squared)
    # TODO: return it rounded to 1 decimal  (round(value, 1))
    pass


if __name__ == "__main__":
    print(bmi(72, 1.75))    # expected: 23.5
    print(bmi(50, 1.60))    # expected: 19.5

"""

"""
Problem 03 - Initials from a name   (Day 2: strings)   [STUB]

Turn a full name into upper-case dotted initials.
Example: "asha ravi rao"  ->  "A.R.R."

Skills: .split(), indexing word[0], .upper(), building a string.

Run:
    python q03_initials.py
"""

def initials(full_name):
    """Return the dotted, upper-case initials of full_name."""
    # TODO: split the name into words with .split()
    # TODO: start with an empty result string
    # TODO: for each word, add its FIRST letter (upper-cased) + "."
    # TODO: return the result
    pass


if __name__ == "__main__":
    print(initials("asha ravi rao"))   # expected: A.R.R.
    print(initials("Sundar Pichai"))   # expected: S.P.
```

"""
"""
Problem 04 - Palindrome check (strings)   (Day 2: slicing & methods)   [STUB]

A palindrome reads the same forwards and backwards, ignoring case and spaces.
Examples: "Race car" -> True,  "hello" -> False,  "Nurses run" -> True.

Skills: .lower(), .replace(), reverse slicing [::-1], == comparison.

Run:
    python q04_string_palindrome.py
"""

def is_palindrome(text):
    """Return True if text is a palindrome (ignoring case and spaces)."""
    # TODO: make a cleaned version: lower-case it, then remove spaces (.replace(" ", ""))
    # TODO: reverse it with slicing  cleaned[::-1]
    # TODO: return whether cleaned == its reverse
    pass


if __name__ == "__main__":
    print(is_palindrome("Race car"))    # expected: True
    print(is_palindrome("hello"))       # expected: False
```


"""
"""
### Problem 05 — Clean & title-case a messy string

Problem 05 - Clean & title-case a messy string   (Day 2: string methods)   [STUB]

Tidy a messy heading: collapse extra spaces and capitalise each word.
Example: "  hELLo    wORLD  "  ->  "Hello World"

Skills: .split(), .capitalize(), " ".join(list), building a list.

Run:
    python q05_clean_title.py
"""
"""

def clean_title(messy):
    """Return messy with single spaces and each word capitalised."""
    # TODO: .split() with no args -> a list of words, extra spaces gone
    # TODO: build a new list where each word is .capitalize()-d
    # TODO: join that list back together with single spaces: " ".join(words)
    pass


if __name__ == "__main__":
    print(clean_title("  hELLo    wORLD  "))   # expected: Hello World
    print(clean_title("the  TODO   list"))     # expected: The Todo List
```

"""

"""
def grade(marks):
    """Return the letter grade for marks, or 'Invalid' if out of range."""
    # TODO: first reject out-of-range marks (< 0 or > 100) -> "Invalid"
    # TODO: then check the HIGHEST band first (>= 90 -> "A")
    # TODO: work downwards with elif: 75, 60, 40
    # TODO: else -> "F"
    pass


if __name__ == "__main__":
    print(grade(95))    # A
    print(grade(72))    # C
    print(grade(150))   # Invalid
```
"""
"""
Problem 07 - Leap year check   (Day 3: logical operators)   [STUB]

A year is a leap year if:
  - it is divisible by 4 AND not divisible by 100, OR
  - it is divisible by 400.
Examples: 2024 -> True, 1900 -> False, 2000 -> True, 2023 -> False.

Skills: modulo %, and / or / not, returning a boolean.

Run:
    python q07_leap_year.py

def is_leap(year):
    """Return True if year is a leap year, else False."""
    # TODO: divisible by 4 and not by 100  ->  (year % 4 == 0 and year % 100 != 0)
    # TODO: OR divisible by 400            ->  or (year % 400 == 0)
    # TODO: return that single boolean expression
    pass


if __name__ == "__main__":
    print(is_leap(2024))   # True
    print(is_leap(1900))   # False
    print(is_leap(2000))   # True
"""


"""
Problem 08 - Sum & count of digits   (Day 4: while loop)   [STUB]

Without converting to a string, return (sum_of_digits, number_of_digits).
Example: 4096  ->  (19, 4)   because 4+0+9+6 = 19 and it has 4 digits.

Skills: while loop, last digit n % 10, drop last digit n // 10, accumulator + counter.

Run:
    python q08_digit_sum.py
"""

def digit_sum(n):
    """Return (sum_of_digits, digit_count) for a non-negative integer n."""
    # TODO: special-case n == 0 -> (0, 1)
    # TODO: start total = 0 and count = 0
    # TODO: while n > 0:  add n % 10 to total, do n = n // 10, count += 1
    # TODO: return (total, count)
    pass


if __name__ == "__main__":
    print(digit_sum(4096))   # expected: (19, 4)
    print(digit_sum(0))      # expected: (0, 1)

"""

"""
Problem 09 - Star triangle pattern   (Day 4: nested loops)   [STUB]

Print a left-aligned triangle of stars with n rows. For n = 4:
    *
    * *
    * * *
    * * * *
Row r has exactly r stars.

Skills: nested loops (outer = rows, inner = stars), building a line string.

Run:
    python q09_pattern_triangle.py
"""

def triangle(n):
    """Print a star triangle with n rows."""
    # TODO: outer loop r from 1 to n -> for r in range(1, n + 1):
    # TODO:   build a line: inner loop adds "* " r times
    # TODO:   print the line (use .rstrip() to drop the trailing space)
    pass


if __name__ == "__main__":
    triangle(4)
```

"""

"""

question 10 

def fibonacci(count):
    """Return a list of the first `count` Fibonacci numbers."""
    # TODO: start a, b = 0, 1  and an empty list `seq`
    # TODO: loop `count` times: append a, then update a, b = b, a + b
    # TODO: return seq
    pass


if __name__ == "__main__":
    print(fibonacci(10))   # expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(fibonacci(1))    # expected: [0]

"""
"""
Problem 11 - Temperature converter   (Day 5: functions & default args)   [STUB]

Write convert(temp, to="C") that converts a temperature.
  - to="F": Celsius -> Fahrenheit   (temp * 9/5 + 32)
  - to="C": Fahrenheit -> Celsius   ((temp - 32) * 5/9)
Round the result to 2 decimals. Default direction is "C".

Skills: def, parameters, a DEFAULT argument, if/elif/else, return.

Run:
    python q11_temperature_converter.py

def convert(temp, to="C"):
    """Convert temp. to='F' means C->F; to='C' means F->C."""
    # TODO: if to == "F":  return round(temp * 9 / 5 + 32, 2)
    # TODO: elif to == "C": return round((temp - 32) * 5 / 9, 2)
    # TODO: else: return None  (unknown target)
    pass


if __name__ == "__main__":
    print(convert(100, to="F"))   # expected: 212.0
    print(convert(98.6))          # expected: 37.0  (default to="C")

"""
"""

Problem 12 - Number stats with *args   (Day 5: *args & return)   [STUB]

Write stats(*numbers) that accepts ANY number of arguments and returns a dict:
  {"min": ..., "max": ..., "avg": ...}
If no numbers are given, return None.
Example: stats(4, 8, 2, 6) -> {"min": 2, "max": 8, "avg": 5.0}

Skills: *args (collect args into a tuple), loop, min/max tracking, len(), return a dict.

Run:
    python q12_number_stats.py


def stats(*numbers):
    """Return {'min','max','avg'} over the given numbers, or None if none."""
    # TODO: if there are no numbers, return None
    # TODO: track total, smallest, largest as you loop over `numbers`
    # TODO: avg = total / len(numbers)
    # TODO: return {"min": smallest, "max": largest, "avg": avg}
    pass


if __name__ == "__main__":
    print(stats(4, 8, 2, 6))   # expected: {'min': 2, 'max': 8, 'avg': 5.0}
    print(stats())             # expected: None

"""


"""
Problem 13 - Word frequency   (Day 6: dictionaries)   [STUB]

Count how many times each word appears in a sentence (case-insensitive) and
return the count dictionary. Then find the single most common word.
Example: "the cat the dog the" -> {"the": 3, "cat": 1, "dog": 1}; top = ("the", 3)

Skills: .lower(), .split(), dict, dict.get(key, 0), looping over .items().

Run:
    python q13_word_frequency.py


def word_freq(sentence):
    """Return a dict mapping each lower-cased word to its count."""
    # TODO: counts = {}
    # TODO: for word in sentence.lower().split():
    # TODO:     counts[word] = counts.get(word, 0) + 1   # 0 if unseen
    # TODO: return counts
    pass


def most_common(sentence):
    """Return (word, count) for the most frequent word."""
    # TODO: get counts via word_freq(sentence)
    # TODO: loop the items, keep the word with the highest count
    pass

if __name__ == "__main__":
    print(word_freq("the cat the dog the"))   # {'the': 3, 'cat': 1, 'dog': 1}
    print(most_common("the cat the dog the")) # ('the', 3)
```

"""

"""
Problem 14 - Compare two lists with sets   (Day 6: sets)   [STUB]

Given two lists, return three SORTED lists:
  - common:  items in BOTH       (set intersection &)
  - only_a:  items only in list_a (set difference -)
  - combined: every unique item   (set union |)
Example: [1,2,3,4] and [3,4,5] -> common [3,4], only_a [1,2], combined [1,2,3,4,5]

Skills: set(), & intersection, - difference, | union, sorted().

Run:
    python q14_set_compare.py

def compare(list_a, list_b):
    """Return (common, only_a, combined) as sorted lists."""
    # TODO: turn both lists into sets
    # TODO: common = set_a & set_b ;  only_a = set_a - set_b ;  combined = set_a | set_b
    # TODO: return them as sorted() lists
    pass


if __name__ == "__main__":
    print(compare([1, 2, 3, 4], [3, 4, 5]))
    # expected: ([3, 4], [1, 2], [1, 2, 3, 4, 5])

"""
"""
Problem 15 - Class gradebook   (Day 6 + 5: dict of lists, functions)   [STUB]

A gradebook maps each student name -> a list of their marks:
    {"Asha": [88, 92, 79], "Ravi": [70, 65, 80], "Meena": [95, 99, 91]}
Write:
  - averages(gradebook): return {name: average_rounded_2}
  - topper(gradebook):   return (name, average) of the student with the best average

Skills: looping a dict's .items(), sum()/len(), nested data (dict of lists),
        calling one function from another, "best so far".

Run:
    python q15_gradebook.py

    
def averages(gradebook):
    """Return {name: average mark rounded to 2 decimals}."""
    # TODO: result = {}
    # TODO: for name, marks in gradebook.items():  result[name] = round(sum(marks)/len(marks), 2)
    # TODO: return result
    pass


def topper(gradebook):
    """Return (name, average) for the student with the highest average."""
    # TODO: get the averages dict
    # TODO: loop it, keep the (name, avg) with the biggest avg ("best so far")
    pass


if __name__ == "__main__":
    book = {"Asha": [88, 92, 79], "Ravi": [70, 65, 80], "Meena": [95, 99, 91]}
    print(averages(book))   # {'Asha': 86.33, 'Ravi': 71.67, 'Meena': 95.0}
    print(topper(book))     # ('Meena', 95.0)

"""
