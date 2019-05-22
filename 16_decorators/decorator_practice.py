def info(arg1, arg2):
    print('Decorator arg1 = ' + str(arg1))
    print('Decorator arg2 = ' + str(arg2))

    def the_real_decorator(function):
        def wrapper(arg1, arg2):
            if arg1 == "strong":
                print("<strong>{0}</strong>".format(function(arg1)))
            else:
                print("<html>{0}</html>".format(function(arg2)))
            return function(arg1, arg2)

        return wrapper

    return the_real_decorator


@info("strong", 'Python')
def doubler(arg, number):
    return arg, number


doubler(1,2)


