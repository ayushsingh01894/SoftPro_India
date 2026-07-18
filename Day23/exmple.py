ls = [10, 20, 5, 20, 15]

largest = 0
second = 0

for num in ls:
    if num > largest:
        second = largest
        largest = num
    elif num < largest and num > second:
        second = num

print(second)

words = "aaabc"
result =""
count = 1 
for i in range(len(words)):
    
    if i < len(words)-1 and words[i]== words[i+1]:
        count +=1
    else:
        result += words[i] + str(count)
        count = 1

print(result)