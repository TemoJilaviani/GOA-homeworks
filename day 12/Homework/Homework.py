#1
num01 = float(input("Enter the first number: "))
num02 = float(input("Enter the second number: "))
num03 = float(input("Enter the third number: "))

print("The arithmetic mean is:", (num01 + num02 + num03) / 3)



#2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

start_num = min(num1, num2)
end_num = max(num1, num2)

for i in range(start_num, end_num + 1):
    cube = i ** 3
    print("The cube of", i, "is:", cube)


#3
print("Choose an operation:")
print("1. Kilometer to Mile")
print("2. Mile to Kilometer")

choice = input("Enter your choice (1 or 2): ")


if choice == "1":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    print(str(kilometers) + " kilometers is equal to " + str(miles) + " miles.")
elif choice == '2':
    miles = float(input("Enter distance in miles: "))
    kilometers = miles * 1.60934
    print(str(miles) + " miles is equal to " + str(kilometers) + " kilometers.")
else:
    print("Wrong decision.")


#4
number = int(input("Enter a number from 1 to 9: "))

if number < 1 or number > 9:
    print("Please enter a number between 1 and 9.")
else:
    multiples = [num for num in range(1, 51) if num % number == 0]
    print("Multiples of " + str(number) + " from 1 to 50: " + str(multiples))



#5
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



#6
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

registration_info = "Thank you for registering! Your name is " + first_name + " " + last_name + ", you are " 
+ str(age) + " years old, and your email is " + email + "."
print(registration_info)


#7
umber = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in str(umber) if digit.isdigit())
print("Sum of digits: " + str(sum_of_digits))