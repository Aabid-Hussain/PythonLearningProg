def fibo(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
for i in range(20):
    print(fibo(i))