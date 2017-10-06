'''Before calling succ
11
After calling succ
'''

# def dec_fun(func):
#     def wrapper(x):
#         print("Before calling "+ func.__name__)
#
#         print(func(x))
#
#         print("After calling "+ func.__name__)
#
#     return wrapper
#
# @dec_fun
# def add_fun(x):
#     return x + 1
#
# add_fun(10)

def fibo(n):
    a,b=0,1
    while n>0:
        yield a
        a,b = b, a+b

x = fibo(1000000000000000000)
print(next(x))
print(next(x))
print(next(x))
print(next(x))


