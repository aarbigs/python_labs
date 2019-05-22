'''
Write a script with a function that demonstrates the use of *args.

'''

def arg_function(*args):
    # for i in args:
    #     print(i*i)
    a,b,c = args
    print(a, b, c)

arg_function(1, 2, 3)

new_list = []
def arg_function2(*args):
    for arg in args:
        new_list.append(arg)
    print(new_list)


arg_function2(1, 2, 3, 4, 5)