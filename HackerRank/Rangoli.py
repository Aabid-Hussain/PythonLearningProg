import string

alpha = string.ascii_lowercase

n = int(input())
rangoli = []
for i in range(n):
    s = '-'.join(alpha[i:n])
    rangoli.append(s[::-1]+s[1:])

width = len(rangoli[0])

for i in range(n-1,0,-1):
    print(rangoli[i].center(width,"-"))

for i in range(n):
    print(rangoli[i].center(width, "-"))


