numbers = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

count_odd = 0

for num in numbers:
    if num % 2 != 0:
        count_odd += 1

print("Count of odd numbers:", count_odd)
