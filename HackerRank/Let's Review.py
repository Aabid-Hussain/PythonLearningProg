n = int(input())

string_input = [input() for _ in range(n)]

for i in string_input:
    print("{} {}".format(i[::2],i[1::2]))

