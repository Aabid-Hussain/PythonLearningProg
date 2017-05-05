'''Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

list_input =[]
for num in range (2000,3201):
    #checking number div by 7 & not by 5
    if num%7==0 and num/5!=0:
        list_input.append(str(num))
#print in a comma-separated sequence.
print ','.join(list_input)