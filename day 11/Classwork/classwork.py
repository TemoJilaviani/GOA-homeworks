#1
my_money = float(input("Enter your money: "))

if my_money > 100:
    print("You have enough money.")
else:
    print("You do not have enough money.")




#2
age = int(input("enter your age: "))

# Check if the age is over eighteen
if age >= 18:
    print("you are adult.")
else:
    print("you are a child.")



#3total = 0
num = 1
 

while num <= 100:
    total += num
    num += 1

print(total)
