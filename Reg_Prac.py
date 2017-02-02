import re

randStr ="This is my number 412-555-1214"

regex = re.compile(r"412-(.*)-(.*)")#r"412-([\d]{3})-([\d]{4})"

matches = re.findall(regex,randStr)

print len(matches)
print matches
for i in matches:
    print i
print matches[0][0]
print matches[0][1]

#