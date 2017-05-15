#Problem
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# you'll have to use a list comprehension in a list comprehension

import random

probList = [x for x in [random.randint(1,1000) for i in range(50)] if x % 9 ==0]

print(probList)
