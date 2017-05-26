'''
Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.
Hints:
Consider use yield
'''


def div_by_7(n):
    i = 0
    while i < n:
        K = i
        if K % 7 == 0:
            yield K

        i += 1


for num in div_by_7(100):

    print("{}".format(num))
