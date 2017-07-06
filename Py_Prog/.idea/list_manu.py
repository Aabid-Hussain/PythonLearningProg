a = [1,2,3,4,5]
d =[]
c =[]
prod =[]
p =1

for i in range (0,len(a)):
    d.append(p)
    p *=a[i]

p =1
for i in range (len(a) -1, -1,-1):
    c.append(p)
    p *=a[i]

#q =[]
#q = c[::-1]

for i in range (0, len(a)):
    prod.append(d[i]*c[::-1][i])

print prod
