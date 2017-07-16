import math

def factors(n):
    input_store = set(element for i in range(1, int(math.sqrt(n))+1)
                      if n%i == 0
                      for element in (i, n//i)
                      )
    return input_store

fac = factors(36)
print("Factors are : {}".format(fac))
if 3 in fac:
    print("YES")
else:
    print("NO")