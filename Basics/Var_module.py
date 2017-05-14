import os
import StringIO
import datetime


'''
numA = input("Enter the first value: ")
numB = input("Enter the Second value: ")

print "The sum of {} & {} is {}".format(numA,numB,(numA+numB))
print "The product of {} & {} is {}".format(numA,numB,(numA*numB))

L1 = [1,2,3,4,5,11,12,13,14,15]
print "The 2nd onward numbers are :{}".format(L1[1:8])
print "The reverse order of numbers are :{}".format(L1[::-1])

First_Name = raw_input("Enter your First Name: ")
Sur_Name = raw_input("Enter your Surname: ")

print "Your Full name is %s" %(First_Name +( Sur_Name))


Str = raw_input("What is your name? ")
print "The 2nd element till 8th elements are :{} ".format(Str[1:8])

'''

L1 = [1,2,3,4,5,6,7,8]
sum = 0
prod = 1
for i in range (0,len(L1)):
    sum += L1[i]
    prod *=L1[i]

print "The sum of List elements : {}".format(sum)
print "The product of List elements : {}".format(prod)






















