num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

start_num = min(num1, num2)
end_num = max(num1, num2)

for i in range(start_num, end_num + 1):
    cube = i ** 5
    print("The cube of", i, "is:", cube)