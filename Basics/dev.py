def gcd(First_Value, Second_Value):
    while First_Value != 0:
        First_Value,Second_Value = (Second_Value%First_Value),First_Value
    return Second_Value

