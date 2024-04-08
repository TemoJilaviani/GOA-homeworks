original_list = [1, 2, 3, 4, 5]

duplicates_list = [item for item in original_list for _ in range(2)]

print("Duplicated list:", duplicates_list)