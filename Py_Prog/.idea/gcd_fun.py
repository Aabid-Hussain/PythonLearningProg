
def gcd(First_Value, Second_Value):
    while First_Value != 0:
        First_Value,Second_Value = (Second_Value%First_Value),First_Value
    return Second_Value

First = input("Enter the first value:")
Second = input("Enter the second value:")

print "The GCD Value of %d and %d is : %d" %(First,Second,gcd(First,Second))



