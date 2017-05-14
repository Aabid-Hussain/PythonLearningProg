# lambda arg1,arg2, ... : expression

sum =  lambda x,y : x+ y

print "Sum = ", sum(5,9)

Can_Vote = (lambda age : True if age >= 18 else False)

print "Can Vote: ", Can_Vote(15)

# use of lambda in list
powerList = [lambda x: x**2, lambda x: x**3, lambda x: x**4 ]
for func in powerList:
    print func(2)

