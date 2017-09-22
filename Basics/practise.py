def decorate_foo(function):
    def wapper(value):
        print("Before calling "+ function.__name__)
        function(value)
        print("After calling "+ function.__name__)

    return wapper

@decorate_foo
def fool_pool(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
fool_pool("Hi")

print("We now decorate foo with f:")
#foo = decorate_foo(fool_pool)
fool_pool(007)

# print("We call foo after decoration:")
# fool_pool(42)

#fun = decorator_fun(fun) -easy notation