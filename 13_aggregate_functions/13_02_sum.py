'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
from math import fsum
numbers = [2, 3, 4, -5]

numbersSum = sum(numbers)
print(numbersSum)

numbersSum = fsum(numbers)
print(numbersSum)

#How is fsum different?