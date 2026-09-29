''' write a python program to show that tuple value cnnot be changed directly. convert
tuple into list, update it, and convert it back into tuple
'''
# Tuple values cannot be changed directly

t = (10, 20, 30)
print("Original tuple:", t)

l = list(t)

l[1] = 50

t = tuple(l)

print("Updated tuple:", t)
