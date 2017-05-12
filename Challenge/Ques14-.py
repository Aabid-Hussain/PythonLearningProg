'''Write a program that accepts a sentence and calculate the number of upper case 
letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

InputData = raw_input("Enter Input: ")

Count = {"UPPER":0, "LOWER":0}

for i in InputData:

    if i.isupper():
        Count["UPPER"] +=1

    elif i.islower():
        Count["LOWER"] +=1
    else:
        pass

print "UPPER {}".format(Count["UPPER"])
print "LOWER {}".format(Count["LOWER"])