#1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
#2. An @symbol
#3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
#4. A period
#5. 2 to 3 lowercase and uppercase letters
import re

emailList = "db@aol.com m@.com @apple.com db@.com eat@email.com 123@mon.co"

regEx = re.findall("[\w.%+-]{1,20}@[\w.-]{2,20}\.[A-Za-z]{2,3}",emailList)

for i in regEx:
    print i




