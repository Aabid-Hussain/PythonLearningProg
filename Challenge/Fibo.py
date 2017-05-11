'''The Fibonacci numbers are the numbers of the following sequence of integer values: 

0,1,1,2,3,5,8,13,21,34,55,89, ... 

The Fibonacci numbers are defined by: 
Fn = Fn-1 + Fn-2 
with F0 = 0 and F1 = 1 

def fibo(n):
    print "0,1"
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print ','.join(str(fibo(7)))   '''

def fiboNew(n):
    a,b = 1, 0
    #print a,",",b,","
    listNew =[]
    for i in range(n):
        a,b = b, a+b
        listNew.append(str(a))
    print ",".join(listNew)

fiboNew(7)