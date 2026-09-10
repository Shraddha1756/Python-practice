'''write a python program to repeated calculate the sum of digit of a a number util 
the result become a single digit.
'''
num = int(input("Enter a number: "))

while num >= 10:
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    num = sum

print("Single digit =", num)
