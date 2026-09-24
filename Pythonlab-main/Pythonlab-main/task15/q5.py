''' write a pp in an input number in a list of numbres in a list and create two seperate 
list for even and odd number.
'''
numbers = [1, 2, 3, 4, 5]

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)
