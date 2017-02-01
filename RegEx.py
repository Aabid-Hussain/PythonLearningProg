#Regular Expressions(Regex) are used to
#1. Search for a specific string in a large amount of data
#2. Verify that a string has the proper format(Email,Phone#)
#3. Find a string and replace it with another string
#4. Format data into the proper form for importing for example

import re

if re.search("ape", "The ape was at the apex"):
    print "There is an ape"

allApes = re.findall("ape.", "The ape was at the apex") # . is used have any char after search element

for i in allApes:
    print i

    theStr = "The ape was at the apex"

    for i in re.finditer("ape.",theStr):

        locTuple = i.span()
        print locTuple
        print (theStr[locTuple[0]:locTuple[1]])

animalStr = "Cat rat mat pat"

allAnimals = re.findall("[crmfp]at",animalStr)#anything starting from crmfp and having 'at"
someAnimals = re.findall("[c-mC-M]at",animalStr)#anything starting b/w C to M and c to m and having 'at'

some_Animals_Again = re.findall("[^Cr]at",animalStr) #Anything starting with except C and having 'at'
for i in allAnimals:
    print i

#Replacement of string after searching pattern

owlFood = "rat cat mat pat"
regex = re.compile("[cr]at") # compile is used to compile regex patter

owlFood = regex.sub("owl",owlFood)#sub meaning substitute "owl" in place of rat and cat
print owlFood

# usage of Raw String "r" for handling backslash \\
randStr = "Here is \\stuff"
print ("Find \\stuff:%s" %(re.search(r"\\stuff",randStr)))

#. for anything, \. for period(.)
# F.B.I. re.findall(".\..\..\.")
# whitespace re.compile("\n") use substitute(sub)to replace it with anything.
#\b : Backspace
#\f : Form Feed
#\r : Carriage Return
#\t : Tab
#\v : Vertical Tab

New_rand =  ''' This is new string of
multiple lines. This string is used
for removable of whitespace'''

print New_rand

reg = re.compile("\n")
New_rand = reg.sub(" ", New_rand)

print New_rand

# \d : [0-9] Anything from 0 to 9
#\D : [^0-9] Anything except 0 to 9

randStr_New ="12345"
print ("Match : %s" %(len(re.findall("\d{2}",randStr_New))))

''' the out will be 2 because it will block of 2 digits at a time. ie first find will
be 12 then 34 and it will drop 5 because it has only one digit. If \d{3} meaning it
will search number containing 3 digits, \d{5,7} meaning number containg mim 5 digits
and max 7 digits'''

#\w : [a-zA-Z0-9_]
#\W : [^a-zA-Z0-9_]

phNum = "412-55-1112"

if re.search("\w{3}-\w{3}-\w{4}",phNum):
    print "This is phone number"
else:
    print "It is invalid phone number"

#\s : [\f\n\r\t\v]
#\S : [^\f\n\r\t\v]


if re.search("\w{2,20}\s\w{2,20}", "Mohammad Aabid"):
    print "It is valid name"

# + one or more char







