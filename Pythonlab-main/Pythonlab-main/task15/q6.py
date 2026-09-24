''' write a pp to rotate a list one position to the right.
'''
numbers = [10, 20 , 30, 40 , 50]
rotated = [numbers[-1]] + numbers[:-1]

print("Original list:" , numbers)
print("Rotated list:" , rotated)
