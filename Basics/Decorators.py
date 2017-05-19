#__Decorators
'''
Decorators solve both of these issues
(1): code duplication
(2): Cluttering main logic of function with additional functionality(
i.e. timing in our example)

common use cases of decorators,
1) logging
2) Timing

'''
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took " + str((end - start) * 1000) + " mil secs")
        return result

    return wrapper

@time_it
def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    end = time.time()
    print("calc_square took " + str((end-start)*1000) + " mil sec")

    return result

@time_it
def calc_cube(numbers):
    start = time.time()

    result = []
    for number in numbers:
        result.append(number * number * number)
    end = time.time()
    print("calc_square took " + str((end - start) * 1000) + " mil sec")

    return result


array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)