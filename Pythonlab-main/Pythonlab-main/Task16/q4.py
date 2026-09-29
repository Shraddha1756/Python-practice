''' write a pp to store repaeted value in atupple and count how many timesa given value appear.
'''
t = (10, 20, 10, 30, 10, 40, 20)

value = int(input("Enter the value to count: "))

count = t.count(value)

print("The value", value, "appears", count, "times.")
