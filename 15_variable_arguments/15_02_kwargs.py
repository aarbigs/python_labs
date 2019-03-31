'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def kwargs_function(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_function(item_1="hello", item_2="world")