#Q2
'''Instance method: rectagle area and perimeter 
prolem: create a rectagle class with the length and breadth. use instance method to calcluate its area 
and'''
# solutio:

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area:", self.length * self.breadth)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.breadth))

r1 = Rectangle(10, 5)
r1.area()
r1.perimeter()
