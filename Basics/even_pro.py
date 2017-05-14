# to check a number as even or odd

num = input("Enter your number to find Even/Odd:")

if not num%2: #if num%2: will return odd values and if not num%2: will return even value
    print "The number is Even"
else:
    print "The number is Odd"