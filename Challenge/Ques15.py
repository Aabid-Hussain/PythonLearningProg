#RecursionConcept
'''
def facto(x):

    print "Num of times facto is called = {}".format(x)

    if x==1:
        return 1

    else:
        res = x * facto(x-1)
        print "intermediate result for ",x,"*factorial(",x-1,"):",res

        return res

print facto(5)

'''

def factorial(x):
    fac =1
    if x==1:
        return 1

    for i in range(2,x+1):
        fac *= i

    return fac

print factorial(5)
