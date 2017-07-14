s = 'ABCDACDA'
sub_s = 'CDA'
count = 0
for i in range(len(s)):
    if s[i]==sub_s[0]:
        if s[i:i+len(sub_s)] == sub_s:
            count +=1

print(count)

print("Count: {}".format(sum(1
    for i in range(len(s)) if s[i:i+len(sub_s)] == sub_s)))
