

def swap_case(s):
    store = ''

    for elements in s:
        if elements in s.lower():
        #if elements in "abcdefghijklmnopqrstuvwxyz":
            # store.append(elements.upper())
            store += elements.upper()
        else:
            # store.append(elements.lower())
            store += elements.lower()

    return store

print(swap_case("HackerRank.com presents \"Pythonist 2\"."))