number = int(input("Enter a number from 1 to 9: "))

if number < 1 or number > 9:
    print("Please enter a number between 1 and 9.")
else:
    multiples = [num for num in range(1, 51) if num % number == 0]
    print("Multiples of " + str(number) + " from 1 to 50: " + str(multiples))