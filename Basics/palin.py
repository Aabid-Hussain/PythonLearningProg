'''
1. take the input as string
2. using for loop, reverse the string
3. using if loop, compare the original string with reversed string
4. if match is true. string is palindrom
5. else string is not palindrom
input: aabbaa


'''

st1 = raw_input("Input: ")
l1 =[]

for i in range(len(st1) -1 , -1, -1):
      l1.append(st1[i])
if list(st1) == l1:
      print "{} is palindrom".format(st1)
else:
      print "{} is not palindrom".format(st1)

