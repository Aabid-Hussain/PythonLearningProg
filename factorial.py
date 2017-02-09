'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8Then, the output should be:
40320  '''

def factorial(numb):
    if numb ==0 or numb ==1:
        return 1
    else:
        return numb*factorial(numb-1)

print "Factorial program is here:"

print factorial(input("Provide input for factorial: "))

