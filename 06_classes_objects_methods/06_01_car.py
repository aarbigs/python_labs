'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def inc_speed(self):
        self.max_speed = self.max_speed + 5

    def print_details(self):
        print(f"{self.model} {self.year} {self.max_speed}")


my_car = Car("honda", 1999, 15)
my_car.print_details()
my_car.inc_speed(5)
my_car.print_details()
new_car = Car("honda", 2018, 25)
new_car.print_details()