#create a function which uses generator

def fibo_gen():
    a, b = 0, 1
    yield a
    yield b

    while True:
        yield a + b
        a, b = b, a + b

for i in fibo_gen():
    if i >= 1000:
        break

    print(i)