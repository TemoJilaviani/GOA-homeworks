age = int(input("Enter your age: "))

if age >= 0 and age < 18:
    print("You are a kid.")
elif age >= 18 and age < 50:
    print("You are an adult.")
else:
    print("You are an old man.")