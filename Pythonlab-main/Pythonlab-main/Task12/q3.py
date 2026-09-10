'''Write  a python program to input a decimal number and reverse it using the built
-in bin() function'''

#solution:

num = int(input("Enter a decimal number: "))

binary = bin(num)

print("Binary =", binary)

# without binary fun

num = int(input("Enter a decimal number: "))

binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = num // 2

print("Binary =", binary)
