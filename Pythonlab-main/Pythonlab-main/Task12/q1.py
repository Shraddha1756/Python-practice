'''' write a python program to check wether a number is a perfect no. A number is perfect if the sum
of its proper divisor is equal to number itself
'''
#solution:

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")
