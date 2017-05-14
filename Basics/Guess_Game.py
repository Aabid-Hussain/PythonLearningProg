#number guessing game

import random

num = 30
ToBeGuessed_Value = int(num*random.random())+1
guess=0
count=0
while guess!=ToBeGuessed_Value:
    guess=input("Enter the value to be guessed:\n")
    count +=1
    if guess>0:
        if guess>ToBeGuessed_Value:
            print "Guessed number is too large\n"
        else:
            print "Guessed number is too small\n"
    else:
        print "Sorry for Quiting:(\n"
        break
else:
    print "Congratulation for guessing correctly:D\n"
    print "You have guessed correctly in %s try"%count