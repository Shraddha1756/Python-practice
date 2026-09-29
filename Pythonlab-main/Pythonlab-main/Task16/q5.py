''' write a pp to check whether a given value ispresent in a tupple if present display in position
'''

t = (10, 20, 30, 40, 50)

value = int(input("Enter the value to search: "))

if value in t:
    position = t.index(value)
    print("Value is present at position:", position)
else:
    print("Value is not present in the tuple")
