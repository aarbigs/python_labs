'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

a = 10
b = float(a)
print(type(b))
c = "10"
d = int(c)
print(type(d))
e = 5.0/2
print(type(e))

f = int(input("Please enter one number: "))
g = int(input("Please enter another number: "))
print(f*g)