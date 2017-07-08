import sys

value = set()
char_store = ''
counter = 0

s = input().strip()
n = int(input().strip())

for c in s:
    if c != char_store:
        counter = 1
        char_store = c
    else:
        counter += 1
    value.add(counter * (ord(c) - 96))

for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    print("Yes" if x in value else "No")