'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Your {self.make} {self.model} is from {self.year}"

# class Car(Vehicle):
#     def __init__(self, make="Honda", model="civic", year="2016"):
#         self.make = make
#         self.model = model
#         self.year = year

my_vehicle = Vehicle("bicycle", 'red', 2000)
print(my_vehicle)
# my_honda = Car()
# print(my_honda)
# my_car = Car("toyota", "4runner", 2009)
# print(my_car)
