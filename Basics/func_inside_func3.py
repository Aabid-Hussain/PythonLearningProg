#polynomials of arbitrary degree

def poly_create(*argms):
    def poly(x):
        res = 0
        degree = len(argms) -1
        for index, coefficient in enumerate(argms):
            res += coefficient * x**(degree - index)
        return res
    return poly

p1 = poly_create(2, 4)

print(p1(2))

#Decorator -

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

# my_func = outer_function()
# my_func()
# my_func()
# my_func()
# my_func()

hi_func = outer_function('Hi')
hi_func()
Bye_func = outer_function('Bye')
Bye_func()