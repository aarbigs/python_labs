'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
from math import pi

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width
        print(f"The area of your rectangle is {self.area}")

    def perimeter(self):
        self.perimeter = (self.length * 2) + (self.width * 2)
        print(f"The perimeter of your rectange is {self.perimeter}")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = pi * (self.radius**2)
        print(f"The area of your circle is {self.area}")

    def circumference(self):
        self.circumference = (2*pi*(self.radius))
        print(f"The circumference of your circle is {self.circumference}")

new_rec = Rectangle(2, 4)
new_rec.area()
new_rec.perimeter()
new_circ = Circle(5)
new_circ.area()
new_circ.circumference()