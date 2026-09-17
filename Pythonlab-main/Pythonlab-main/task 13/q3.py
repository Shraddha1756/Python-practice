'''write a python proram to print a right-angled trianle using star.
'''
#solution:

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
