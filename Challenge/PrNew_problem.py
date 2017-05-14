from math import sqrt
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        #p = primes(int(sqrt(n)))
        no_p = {j for i in range(2, int(sqrt(n))) for j in range(i*2, n+1, i)}
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p

for i in range(1,50):
    p = primes(i)

print list(p)