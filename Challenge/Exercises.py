'''
Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3
'''


def NewFuct(n):

    if n == 1:
        return 3
    else:
        return NewFuct(n-1) * 3

for i in range(1,11):
    print NewFuct(i)

