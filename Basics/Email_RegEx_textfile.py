#1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
#2. An @symbol
#3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
#4. A period
#5. 2 to 3 lowercase and uppercase letters

import re

#open the file in read mode
fob = open("E:\ME\PythonLearningProg\\textfile\mailContent.txt", "r+")
#open the file in Write mode
dob = open("E:\ME\PythonLearningProg\\textfile\NewmailContent.txt","w+")

for i in fob.readlines():
    re1 = i
    reg = re.findall("[\w.%+-]{1,20}@[\w.-]{2,20}\.[A-Za-z]{2,3}\s",re1)
    dob.writelines(reg) # write pattern matched output in file

fob.close()

#\w : [A-Za-z0-9_]
#1 to 20 lowercase and uppercase letters, numbers, plus ._%+- RegEx[\w.%+-]{1,20}