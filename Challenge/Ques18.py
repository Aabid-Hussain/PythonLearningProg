'''
A website requires the users to input username and password to register. Write a program to check the 
validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according 
to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
import re

'''
pass_word = input("Enter the input: ").split(',')
# reg_ex = str(pass_word)
# print(reg_ex)
match = re.search(r'([a-zA-Z0-9$#@]+){6,12}', str(pass_word))
if match:
    print(match[0])

#
# RawData = input("Enter the input: ")
#
# word_list = [word for word in RawData.split(',')]
# # print(word_list)
# # 1. At least 1 letter between [a-z]

RegEx = re.search(r"([a-zA-Z0-9$#@]+){6,12}",str(input("Enter Input")))
# for word in word_list:
#     # if len(word) >= 6 and len(word) <= 12:
if RegEx:
    print(RegEx[0])

# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12

'''








