def get_primes(input_list):
    result_list = list()

    if is_prime(input_list):
        result_list.append(input_list)
    return result_list

# or better yet...
'''
def get_primes1(input_list):
    return (element for element in input_list if is_prime(element))
'''
# not germane to the example, but here's a possible implementation of
# is_prime...
import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


primeCheck = range(1, 100)
for p in primeCheck:
    print get_primes(p)
