''' write a pp program to print a square patttern of star for n row and n coloumn
'''
#solution:

n = int(input("Enter n: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
