#program to use multiple arguments in function using python

def SumAll(*arg):
    Sum =0

    for var in arg:
        Sum +=var

    return "Sum: {}".format(Sum)


print SumAll(10,12,15,10)


