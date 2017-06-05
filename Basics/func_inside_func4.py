#Decorator - it is function that takes another function as it's argument.
            # and add some kind of functionality and return a function without
            # altering the original source code function which is passed in
'''
meaning of @decorator_functions
display = decorator_functions(display)

TypeError: wrapper_function() takes 0 positional arguments but 2 were given
positional argument is defined using = *var
Keyword argument is defined using = **var
General practice [positional] arg = *args; [keyword] arg = **kwargs
'''
def decorator_functions(func):
    def wrapper():
        print("{} function executed before {} function".format(
            wrapper.__name__, func.__name__))
        return func()

    return wrapper


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("{} function executed before {} function".format(
            wrapper.__name__, func.__name__))
        return func(*args, **kwargs)

    return wrapper

#class used as decorator
class decorators:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("call method executed before {} functions".format(
             self.func.__name__))

        return self.func(*args, **kwargs)


@decorator_functions
def display():
    print('display function ran')
    print()

display()

@decorators
def display_info(name, age):
    print('display_info ran with arguments ({},{})'.format(name, age))
    print()

display_info('Aabid', 25)

