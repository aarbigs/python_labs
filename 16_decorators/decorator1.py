def print_function(name):
    print(f"Hello my name is {name}")

#print_function("Aaron")

def say_hello(name1, name2):
    print(f"Hello {name1} and {name2}")

def be_awesome(name):
    print(f"Yo {name}, together we are the awesomest!")

def greet_bob(greeter_func, name1):
    return greeter_func(name1)

#greet_bob(say_hello, "Aaron", "Gilad")

greet_bob(be_awesome,"aaron")