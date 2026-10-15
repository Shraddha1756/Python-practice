''' crate a class & and object:Student details 
problems : create a student  cklass to store student  name and roll no.
create an oject ad display using an instace method.
'''
#solutio:

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

s1 = Student("Shraddha", 34)
s1.display()
