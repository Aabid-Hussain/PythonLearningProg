'''
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")
'''

def decor(func):
    def decor_wrapper(x):
        print("before function called " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return decor_wrapper

@decor
def foo(x):
    print("foo is called with " + str(x))

foo("python")



