import sys
import re

n = int(input())
binary_value = bin(n).lstrip('0b')
binary_value1 = binary_value[::-1]
ch = ''
count = 0
dcount = 0
for i in range(len(binary_value)):
    if binary_value[i] == '1':
        count += 1
    else:
        break
for j in range(len(binary_value1)):


    if binary_value1[j] == '1':
        dcount += 1
    else:
        break

print(max(count,dcount))

#simple and sort
# print(len(max(re.split("0+",bin(int(input().strip()))[2:]))))

input_store = (bin(int(input())))[2:]

tem_store = re.split(r"0+", input_store)
print(len(max(tem_store)))