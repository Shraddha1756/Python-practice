''' write a pp to list of number and createa new list containing only unique element.
'''
numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Unique list:", unique)
