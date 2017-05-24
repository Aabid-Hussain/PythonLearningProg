def printData():
    # a = "0"
    """This function prints statement whenever called"""

    print("printData is called :) ")

    return ":D"


print(printData.__doc__) # Docstring

#functionName.__doc__ will give the first statement in the body of
# of a function is usually a string.

print(printData())



def no_return(x,y):
    c = x + y
    return c

res = no_return(4,5)
print(res)

