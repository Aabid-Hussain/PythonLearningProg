def natural(func_name):

    def checking_fun(x):
        if type(x)==int and x>0:
            return func_name(x)
        else:
            print("number is not natural")

    return checking_fun



@natural
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

for i in range(0,10):
    print (i, fact(i))

