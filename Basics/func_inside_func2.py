#Functions returning Functions

def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

print(nf1(1))
print(nf2(1))

# formula for polynomials with degree 2: p(x) = a.x**2 + b.x + c

def poly_constant(a, b, c):

    def poly_variable(x):
        return (a * x**2 + b*x + c)

    return poly_variable

p1 = poly_constant(2, 3, 4)
p2 = poly_constant(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))

