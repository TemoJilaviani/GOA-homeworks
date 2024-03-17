number = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in str(number) if digit.isdigit())
print("Sum of digits: " + str(sum_of_digits))