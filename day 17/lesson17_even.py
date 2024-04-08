inputs = [int(input("Please enter a number: ")) for i in range(5)]

even_numbers = [num for num in inputs if num % 2 == 0]

print(even_numbers)