'''Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

randStr =[]
for digit in range(1000,3001):

    strConv = str(digit)

    if int(strConv[0])%2==0 and int(strConv[1])%2==0 and int(strConv[2])%2==0 \
        and int(strConv[3])%2==0:

        randStr.append(str(digit))

print ",".join(randStr)
