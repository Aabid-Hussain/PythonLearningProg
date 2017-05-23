def itemgetter(*items):
    # for i in items:
    #     print(i)
    if len(items) == 1:
        item = items[0]
        def g(ob):
            print(ob)
            return ob[item]
    else:
        def g(ob):
            print(ob)
            return tuple(ob[item] for item in items)
    return g

print(itemgetter(1, 3, 5)('ABCDEFG'))