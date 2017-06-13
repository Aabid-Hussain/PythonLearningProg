'''
Tail Recursive: a function is said to be tail recursive
 if there is nothing to do after the function returns except
 return its value
'''

def tail_function1(n):
    if n == 0:
        return 0
    else:
        return (n + tail_function1(n-1))

def tail_function2(n, result):
    if n == 0:
        return (result)

    else:
        return tail_function2(n-1, n + result)

print("Tail Function 1 is called and output is : {}".format(tail_function1(5)))
print("Tail Function 2 is called and output is : {}".format(tail_function2(5, 0)))