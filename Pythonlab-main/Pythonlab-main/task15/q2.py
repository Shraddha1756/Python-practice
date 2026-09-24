''' write a python program to input marks 10 student .store only a vlaid marks between 0and 100 in alist
skip invaid marks
'''
marks = []

for i in range(10):
    m = int(input("Enter marks: "))

    if 0 <= m <= 100:
        marks.append(m)
    else:
        continue

print("Valid marks:", marks)
