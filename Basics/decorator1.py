def natural_num(func):
    #def wrapper(*args, **kwargs):
    def helper(x):
        if type(x) == int and x > 0:
            return func(x)
        else:
            raise Exception("Argument is not integer")
    return helper


@natural_num
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(-1))
print()
for i in range(1,10):
    print(i, fact(i))


