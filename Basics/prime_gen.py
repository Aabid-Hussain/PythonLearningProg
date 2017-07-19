def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if not n%i :
                return False
        else:
            return True

# for n in range(2,101):
#     if is_prime(n):
#         print("{}".format(n), sep="\n")

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

for i in prime_generator():
    if i>100:
        break
    print(i)

'''   
# primes up to 'max'
def primes_max(max):
    yield 2
    for n in range(3, max, 2):
        if is_prime(n):
            yield n

# the first 'count' primes
def primes_count(count):
    counter = 0
    num = 3

    yield 2

    while counter < count:
        if is_prime(num):
            yield num
            counter += 1
        num += 2

'''