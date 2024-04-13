#1
age = int(input("Please enter your age: "))

if age < 18:
        print("You are a minor.")
elif age >= 18 and age < 65:
        print("You are an adult.")
else:
        print("You are a senior citizen.")



#2
for i in range(10, 0, -1):
    print(i)




#3
for o in range(5):
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        print(str(num) + " is even.")
    else:
        print(str(num) + " is odd.")



#4
grade = input("please enter your letter grade (A, B, C, D, or F): ")


if grade == 'A':
        print("excellent!")
elif grade == 'B':
        print("good job!")
elif grade == 'C':
        print("you passed.")
elif grade == 'D':
        print("you can do better.")
elif grade == 'F':
        print("you failed.")
else:
        print("invalid grade.")




#5
number = 8

for u in range(1, 11):
    print(number * u)




#6
number = 1

while number <= 10:
        print(number)
        number += 1




#7
import random

random_number = random.choice(range(1, 11))

while True:
    guess = int(input("guess a number between 1 and 10: "))
    
    if guess == random_number:
        print("congratulations! correct number.")
        break
    else:
        print("try again!")
