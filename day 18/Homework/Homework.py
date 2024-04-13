#1
original_list = [1, 2, 3, 4, 5]

duplicates_list = [item for item in original_list for i in range(2)]

print("Duplicated list:", duplicates_list)



#2
numbers = [1, 2, 3, 4, 5]

if numbers:
    print("The mean of the list is:", sum(numbers) / len(numbers))
else:
    print("The list is empty. Cannot calculate mean.")



#3
numbers1 = [10, -5, 8, -3, 0, -2]
result = [num for num in numbers1 if num >= 0]
print(result)



#4
nums_for_list1 = [int(input("Enter number for the first list: ")) for i in range(5)]
nums_for_list2 = [int(input("Enter number for the second list: ")) for i in range(5)]

list1 = [nums_for_list1]
list2 = [nums_for_list2]

merged_list = list1 + list2

print(merged_list)