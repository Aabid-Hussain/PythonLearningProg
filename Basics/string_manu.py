#to work with string operations

# to capitalize first char of string
str = "this is my string"

str_New = str.capitalize()

print (str_New)

#to upper case string

Str = "This is my string"
print (str.upper())

#to lower case string

str= "This is my string"
print (str.lower())

#to slice a string str[::-1] is used to reverse string

str = "This is my string"
slice_Object = slice(3,8)
print (str[slice_Object])



# to count char repeatation in a given string
str = "Let's play with strings"
#count('searching char',start, stop of string length
print "The count of I is:", str.upper().count('I',0,len(str))


#to use lstrip() and rstrip() functions

str = "88888888888Let's play with strings8888888888"
str_New = str.lstrip('8')
print str_New,"\n",str.rstrip('8')

#usage of both left hand side strip and right hand side strip
'''lstrip() method is used to strip returns a copy of the string
in which all chars have been stripped from the beginning if the
string(default whitespace characters). '''

print str.lstrip('8').rstrip('8')

str_New = "method is used to strip returns a copy of the string \
in which all chars have been stripped"

str_New_split = str_New.split(' ')
print str_New.split(' ')
for i in str_New_split:
    print i

str_New_replace = str_New.replace(' ','',len(str_New))
print str_New_replace
print str_New
#to reverse a string: [::-1]

print str_New[::-1]