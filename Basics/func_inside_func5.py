#usage of class as decorator

class decorators:

    def __init__ (self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Call Method is executed before {} function".format(
                    self.func.__name__))

        return self.func(*args, **kwargs)

@decorators
def addition(arg1,arg2):
    return (arg1 + arg2)

print("Sum: {}".format(addition(10,20)))

