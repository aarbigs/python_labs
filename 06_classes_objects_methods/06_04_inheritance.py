'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
import django

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Your {self.make} {self.model} is from {self.year}"

class Car(Vehicle):
    def __init__(self, make="Honda", model="civic", year="2016"):
        self.make = make
        self.model = model
        self.year = year

class Toyota(Car):
    def __init__(self, make="Toyota", model="camry", year="2018"):
        self.make = make
        self.model = model
        self.year = year

my_vehicle = Vehicle("bicycle", 'red', 2000)
print(my_vehicle)
my_honda = Car()
print(my_honda)
my_car = Car("toyota", "4runner", 2009)
print(my_car)
my_toyota = Toyota()
print(my_toyota)