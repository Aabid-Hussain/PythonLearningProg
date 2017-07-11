class Addition:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value
        return self.__a

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, value):
        self.__b = value
        return self.__b

    def __str__(self):
        return "NewResult({},{})".format(int(self.a), int(self.b))


    def __add__(self, other):
        return Addition(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Addition(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Addition(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Addition(self.a / other.a, self.b / other.b)

    def __floordiv__(self, other):
        return Addition(self.a // other.a, self.b // other.b)

    def __mod__(self, other):
        return Addition(self.a % other.a, self.b % other.b)


add1 = Addition(12,24)
add2 = Addition(5,10)

print(add1 + add2)
print(add1 - add2)
print(add1 * add2)
print(add1 / add2)
print(add1 // add2)
print(add1 % add2)
