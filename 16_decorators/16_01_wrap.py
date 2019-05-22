'''
Write a decorator function that wraps text passed to it in a specified html tag.
The user should be able to decide which tag to use.

'''


# def strong_decorate(func):
#     def func_wrapper(name):
#         return "<strong>{0}</strong>".format(func(name))
#     return func_wrapper


def html_tag(func):
    #I will now create within this function a new function
    def func_wrapper(name, html):
        #my inner function has access to the variable "func" in the outer scope
        return f"<{html}>{func(name)}</{html}>"

    return func_wrapper


@html_tag
def print_twice(text2):
    return f"{text2}"*2

print(print_twice("hello", 2))

