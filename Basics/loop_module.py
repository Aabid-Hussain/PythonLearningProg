
#1.Write a program to print all numbers between 0 to 50
for i in range (1,50):
    print i

#Write a program to print all even numbers between 1 to 50
for i in range (1,50):
    if i%2==0:
        print i

#3.Write a program to print all off numbers between 1 to 50
for i in range (1,50):
    if i%2 != 0:
        print i

#4.Write a program to print all elements of list in different line
List_1 =[2,5,3,4,"apple",7,"mango",40]
    #["apple","Bananas","mango",'litche','strawberry',"pineapple"]
for i in range (0, len(List_1)):
    print List_1[i],

#5.write a program to print all elements of list in same line
Str_New = "My pet name is boxer"

#6.Write a program to print all characters of a string "My pet name is boxer" in each line
for i in range (0,len(Str_New)):
    print Str_New[i]

#7.Write a program to print even number using increment parameter of range command.
for i in range(2,50,2):
    print i

#8.Write a program to take input from user a number and check if it is prime number or not
Num = input("Enter a number to verify Prime: ")
if Num>1:
    for i in range (3,int(Num*0.5)+1,2):
        if Num%i==0:
            print "Not Prime"
            break
    else:
        print "Prime"

else:
    print "Not Prime"

#9.Print the prime number in between 2 to 50
for num in range (2,50):
    if num>1:
        for i in range (2,int(num*0.5)+1):
            if (num%i==0):
                break
        else:
            print num


#10.Write a Python program to find power of any number using for loop.
base = input("Enter the base value: ")
power = input("Enter the power of base value: ")
value = 1
for i in range (0,power):
    value *=base

print "The {} to power {} = {}".format(base,power,value)


#11.write a program to print the number of vowels in the given word using dictionary

Vow_Input = raw_input("Enter the string: ")
Vow_Input = Vow_Input.lower()

count={x:sum([1 for char in Vow_Input if char == x])for x in 'aeiou'}

print count


#12.write a program to check if the given string is a palindrome or not

Palin = raw_input("Enter the string: ")

Palin =Palin.lower()

Rev_Palin =reversed(Palin)

if list(Palin)== list(Rev_Palin):
    print "Palindrom"
else:
    print "Not Palindrom"

#13.write a program to remove the duplicate elements in the list. array =[1, 2, 3, 4, 5, 2, 3, 4]

length = input("Enter the length of list: ")
array =[]
a=0
List_New = []

#for loop is used to take input()
for i in range (0,length):
    # array = [1, 2, 3, 4, 5, 2, 3, 4]
    a =input("Enter the {}th element of the Array\n".format(i))
    array.append(a)

for i in array:
    if i not in List_New:
        List_New.append(i)

print List_New



var = []
#a = 0
new_var = []
range_limit = input("Enter the range limit: ")

for i in range(0,range_limit):
    a = input("enter {} element: \n".format(i+1))
    var.append(a)

for i in var:
    if i not in new_var:
        new_var.append(i)
        new_var.sort()

print new_var

#14.Write a program to count number of time each element of list is repeated. It should not print for Duplicate number the count"

var = []
count =0
range_limit = input("Enter the limit:\n")

for i in range (0,range_limit):
    var.append(input("Enter the {} element: \n".format(i+1)))

new_var =[]

for i in var:
    if i not in new_var:
        new_var.append(i)

for j in new_var:
    for k in var:
        if j==k:
            count =count +1

    print "{} is {} time \n".format(j,count)
    count =0

#15.Write a python script to find non-repeating character in string

str ='Goodboy'
print [x for x in str if str.count(x)==1]



#16.Write a program to Reverse a number without converting it into string.

num=num1 =input('Enter the number to be reversed:',)
Num_New =0

while num >0:
    Num_New =(Num_New + num%10)*10
    num /=10

print "{} is the reversed of {}".format(Num_New/10,num1)


#18.Write a program which will find all such numbers which are divisible by 7 but
#are not a multiple of 5,between 2000 and 3200 (both included).The numbers obtained
#should be printed in a comma-separated sequence on a single line.

store =[]
for num in range(2000,3201):
    if num%7==0 and num%5 !=0:
        store.append(num)

print store



#19.With a given integral number n, write a program to generate
#a dictionary that contains (i, i*i)such that is an integral
#number between 1 and n (both included). and then
# the program should print the dictionary.Hint(Q19):
# "Suppose the following input is supplied to the program:
# 8 Then, The output should be:
#{1:1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7:49, 8: 64}

limit = input("Enter the limit of Square sequence: ")
square ={i:(i*i) for i in range (1,limit+1)}
print square


#20.Write a program that accepts a comma separated sequence
# of words as input and prints the words in a comma-separated
#  sequence after sorting them alphabetically. Hint(Q20):
# "Suppose the following input is supplied to the program:
# without,hello,bag,world Then,the output should be:
#bag,hello,without,world"


st = raw_input("Enter the sequence of words with comma separation: ")
st_new = st.split(',')
st_new.sort()

print "The sorted worlds alphabetically are as follow:\n %s" %(st_new)






































