#1
multiples_of_4 = [num for num in range(10, 51) if num % 4 == 0]

print(multiples_of_4)



#2
numbers01 = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

count_odd = 0

for num in numbers01:
    if num % 2 != 0:
        count_odd += 1

print("Count of odd numbers:", count_odd)



#3
inputs = [int(input("Please enter a number: ")) for i in range(5)]

even_numbers = [num for num in inputs if num % 2 == 0]

print(even_numbers)



#4
games = ["FIFA", "GTA 5", "Roblox"]

games[0] = "sololearn"
games[1] = "w3"
games[2] = "codewars"

print(games)


        


#5
numbers = [78, 80, 3, 15, 11, 65, 96, 48, 100, 27]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print("The biggest number is:", biggest)



#6
number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))
number3 = int(input("Please enter third number: "))
number4 = int(input("Please enter fourth number: "))
number5 = int(input("Please enter fifth number: "))

print(number1 + number2 + number3 + number4 + number5)