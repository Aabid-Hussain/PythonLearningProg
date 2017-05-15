def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def get_number(range_num):

    for num1 in range(2,range_num):

        if is_prime(num1):
            yield num1

prime = get_number(100)

print("Prime : ", next(prime))
print("Prime : ", next(prime))
print("Prime : ", next(prime))
print("Prime : ", next(prime))
print("Prime : ", next(prime))
print("Prime : ", next(prime))

import random

double = (x * 2 for x in [random.randint(1,50) for i in range(10)])

print("Double :",next(double))
print("Double :",next(double))
print("Double :",next(double))
