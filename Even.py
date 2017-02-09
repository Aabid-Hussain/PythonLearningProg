# 2	Write a program to print all even numbers between 1 to 50

print "Numbers between 1 to 50:"

for i in range(1,50):
    if i%2==0: #can be used "if not i%2:" --> return 0
        # if i%2: --> return any value but not 0
        print i