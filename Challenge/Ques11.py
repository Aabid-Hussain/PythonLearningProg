'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as 
its input and then check whether they are divisible by 5 or not. The numbers that are divisible 
by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001,1111
Then the output should be:
1010'''

RandStr = []

items = [x for x in raw_input("Enter Input: ").split(",")]

for i in items:
    inputData = int(i,2)
    if inputData%5==0: # if not inputData%5:
        RandStr.append(i)


print ",".join(RandStr)