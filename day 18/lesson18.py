nums_for_list1 = [int(input("Enter number for the first list: ")) for _ in range(5)]
nums_for_list2 = [int(input("Enter number for the second list: ")) for _ in range(5)]

list1 = [nums_for_list1]
list2 = [nums_for_list2]

merged_list = list1 + list2

print(merged_list)