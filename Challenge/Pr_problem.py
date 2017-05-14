# to check if number is prime or not
# prime - a number which is divisible by one and itself is called prime
# prime start from 2.
# imp point, to verify that if a number is not divisible by seq of number untill sqrt of its own number
# then the number is prime

import math


def prime(num):
    if num == 2:
        return True
    elif num == 1:
        return False
    else:
        for iteration in range(2, int(math.sqrt(num))):

            if num % iteration == 0:
                return False
        else:
            return True

numList = input("Enter limit: ")
primeSet = []
for i in range(2, numList):
    if prime(i):
        primeSet.append(i)

print primeSet


