#Question 1

number = int(input("Enter a number: "))
original_number = number
number += 6
number -= 4
number *= 2
number /= 2
number = original_number

print("Starting number:", original_number)
print("Result", number)

#Question 2
# Calculate seconds in a day
seconds_in_a_day = 24 * 60 * 60
# Calculate seconds in a week
seconds_in_a_week = seconds_in_a_day * 7
# Calculate seconds in a year (365 days)
seconds_in_a_year = seconds_in_a_day * 365
# Print the results
print("Seconds in a day:", seconds_in_a_day)
print("Seconds in a week:", seconds_in_a_week)
print("Seconds in a year:", seconds_in_a_year)


#Question 3

bill_amount = 2400
number_of_friends = 5
tip_percentage = 0.10
# Calculate the total tip
tip_amount = bill_amount * tip_percentage
# Calculate the total amount including tip
total_amount = bill_amount + tip_amount
# Calculate the amount each person pays
amount_per_person = total_amount / number_of_friends
print("Each person pays:", amount_per_person)
