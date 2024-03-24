import random

random_number = random.choice(range(1, 11))

while True:
    guess = int(input("guess a number between 1 and 10: "))
    
    if guess == random_number:
        print("congratulations! correct number.")
        break
    else:
        print("try again!")