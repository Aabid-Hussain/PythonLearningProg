'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

randStr = raw_input("Enter Input: ")
wordLetter = {"LETTERS":0,"DIGITS":0}
for items in randStr:

    if items.isdigit():
        wordLetter["DIGITS"] +=1

    if items.isalpha():
        wordLetter["LETTERS"] +=1

print "LETTERS {}".format(wordLetter["LETTERS"])
print "DIGITS {}".format(wordLetter["DIGITS"])

