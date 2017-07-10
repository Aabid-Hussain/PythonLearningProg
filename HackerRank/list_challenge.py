value_store = []
N = int(input())
for i in range(N):
    a = input().strip().split(' ')

    if a[0] == 'insert':
        value_store.insert(int(a[1]), int(a[2]))

    elif a[0] == 'print':
        print(value_store)

    elif a[0] == 'remove':
        value_store.remove(int(a[1]))

    elif a[0] == 'append':
        value_store.append(int(a[1]))

    elif a[0] == 'sort':
        value_store.sort()

    elif a[0] == 'pop':
        value_store.pop()

    else:
        if a[0] == 'reverse':
            value_store.reverse()
