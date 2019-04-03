'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''
from functools import reduce

items = [1, 2, 3]
#sum_3 = lambda x,y,z: x +y+z
#print(sum_3(1,2,3))

sum_map = reduce((lambda x,y: x+y), [1,2,3])
print(sum_map)