''' write the python program to store multiple student record as a list of record as alist of tuple.
each tupple should contain name, roll number, and marks. display student who scared above 75.
'''

students = [
    ("Shraddha", 101, 85),
    ("Tanish", 102, 72),
    ("Ananya", 103, 90),
    ("Rahul", 104, 68),
    ("Priya", 105, 78)
]

print("Students who scored above 75:")

for student in students:
    if student[2] > 75:
        print("Name:", student[0])
        print("Roll Number:", student[1])
        print("Marks:", student[2])
        print()
