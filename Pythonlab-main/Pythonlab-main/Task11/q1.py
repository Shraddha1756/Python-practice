'''Write a python program to input four number  from the user and find the greatest among them
'''
#solution:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

greatest = max(a, b, c, d)

print("Greatest number is:", greatest)
