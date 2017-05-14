#------------------PROBLEM-------------
# Create a random list filled with the characters H and T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads : 46
# Tails : 54

import random

#Create a empty list
randomList = []

#Populate the list with 100 Hs and Ts

for i in range(1,101):
    randomList += random.choice(['H','T'])

#Output the results

print "Heads : ", randomList.count(('H'))
print "Tails : ", randomList.count('T')