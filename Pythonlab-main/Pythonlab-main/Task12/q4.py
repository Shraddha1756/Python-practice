'''Write a python program to print number from 1 t0 50 , but skip all number disable by 4.
'''
#solution:

for i in range(1, 51):
    if i % 4 == 0:
        continue
    print(i)
