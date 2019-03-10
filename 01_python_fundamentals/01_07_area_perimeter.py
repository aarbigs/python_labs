'''

Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.4 and a height of 6.4.

'''
import math

width = 2.4
height = 6.4
area = width * height
hypotenus = math.sqrt(width**2 + height**2)
perimeter = width + height + hypotenus
print(area)
print(perimeter)