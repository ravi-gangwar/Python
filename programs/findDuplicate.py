def find_duplicates(numbers):
    seen = set()
    duplicates = []

    for num in numbers:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
list_of_duplicates = find_duplicates(list1)
print(list_of_duplicates)
print("-----------------------------------------------------")
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = find_duplicates(list2)
print(list_2)

