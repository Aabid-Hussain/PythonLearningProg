def f():
    print(s)
s = "Python"
f()

def f():
    s = "Perl"
    print(s)

s = "Python"
f()
print(s)

def f():
    print(s)
    s = "Perl"
    print(s)


s = "Python"
f()
print(s)


def f():
    global s
    print(s)
    s = "dog"
    print(s)
s = "cat"
f()
print(s)