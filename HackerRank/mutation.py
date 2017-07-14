string = "abracadabra"
string1 = list(string)
string1[5] = 'k'

print(''.join(string1))

print(string[:5] + 'M' + string[6:])

print(string[:5])
print(string[6:])