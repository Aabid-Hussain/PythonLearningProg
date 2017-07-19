def is_prime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if not n%i:
                return False
        else:
            return True

def prime_gen():
    n = 2
    while True:
        if is_prime(n):
            yield n

        n += 1

for i in prime_gen():
    if i>100:
        break

    print(i)