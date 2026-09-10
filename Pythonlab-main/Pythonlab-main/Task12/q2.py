'''write the python program to input a number and reverse it using airthemetic operation only.
'''
#solution:
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse =", rev)
