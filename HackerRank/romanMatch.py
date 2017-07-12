import re
m = re.match(r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', input())
print (bool(m))


from roman import fromRoman
x = input()
try:
    if (fromRoman(x)>0 and fromRoman(x)<4000):
        print(True)
    else:
        print(False)
except:
    print(False)
