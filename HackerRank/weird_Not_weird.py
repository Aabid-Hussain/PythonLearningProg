n = int(input())

# If n is odd, print Weird

if n%2:
    print("Weird")

else:

# If n is even and in the inclusive range of 2 to 5, print Not Weird

    if n in range(2,6):
        print("Not Weird")

# If n is even and in the inclusive range of 6 to 20, print Weird

    elif n in range(6,21):
        print("Weird")

# If 20 is even and greater than , print Not Weird
    else:
        print("Not Weird")




