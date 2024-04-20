#1
def numbers_product(start, end, step):
    numbers_list = []
    
    current_number = start
    
    while current_number <= end:
        if current_number % 3 == 0:
            numbers_list.append(current_number)
        current_number += step

    product = 1

    for number in numbers_list:
        product *= number
    
    return product

start = 1
end = 20
step = 2
result = numbers_product(start, end, step)
print("Product of multiples of 3:", result)








#2
def numbers_product(start, end, step):
    numbers_list = []
    current_number = start
    while current_number <= end:
        if current_number % 3 == 0:
            numbers_list.append(current_number)
        current_number += step
    product = 1
    for number in numbers_list:
        product *= number
    return product

result = numbers_product(1, 20, 2)

def perform_operation(operation, second_number):
    if operation == '+':
        return result + second_number
    elif operation == '-':
        return result - second_number
    elif operation == '*':
        return result * second_number
    elif operation == '/':
        if second_number != 0:
            return result / second_number
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

operation = input("Enter the operation (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

result_of_operation = perform_operation(operation, second_number)
print("Result of operation:", result_of_operation)




#3
def hashtag_generator(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(capitalized_words)
    return hashtag

sentence = input("Enter a sentence: ")
result = hashtag_generator(sentence)
print("Generated Hashtag:", result)




#4
def num_divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return divisors

user_number = int(input("Enter an integer: "))
result = num_divisors(user_number)
print("Divisors:", result)



#5
def manual_split(word, start, end, step):
    result = ""
    for i in range(start, end, step):
        result += word[i]
    return result

word = input("Enter a word: ")
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
step = int(input("Enter the step value: "))

result = manual_split(word, start, end, step)
print("Result:", result)


