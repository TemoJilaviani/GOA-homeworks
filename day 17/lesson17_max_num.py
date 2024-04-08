numbers = [78, 80, 3, 15, 11, 65, 96, 48, 100, 27]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print("The biggest number is:", biggest)