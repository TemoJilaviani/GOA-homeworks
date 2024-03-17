print("Choose an operation:")
print("1. Kilometer to Mile")
print("2. Mile to Kilometer")

choice = input("Enter your choice (1 or 2): ")


if choice == "1":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    print(f"{kilometers} kilometers is equal to {miles} miles.")
elif choice == '2':
    miles = float(input("Enter distance in miles: "))
    kilometers = miles * 1.60934
    print(f"{miles} miles is equal to {kilometers} kilometers.")
else:
    print("Wrong decision.")
