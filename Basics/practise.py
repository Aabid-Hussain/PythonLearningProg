'''class A:
    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)


x = A()
print("now calling the instance:")
x(3, 4, x=11, y=10)
print("Let's call it again:")
x(3, 4, x=11, y=10)


class Fibonacci:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")'''

# range and xrange used similarly just for iterable,
# main difference is range returns python list obj and
# xrange returns python xrange object

class Fibo:
    def __init__(self):
        self.container = {}

    def __call__(self, n):
        if n not in self.container:
            if n == 0:
                self.container[0] = 0
            elif n==1:
                self.container[1] = 1
            else:

                self.container[n] = self.__call__(n-1) \
                                    + self.__call__(n-2)
        return self.container[n]

fibo = Fibo()

for i in range(111):
    print(fibo(i))

import pyshark
import time

cap = pyshark.FileCapture("E:\ME\Lab\RIP\BGP_routes.pcapng")

for i in cap:
    print i
    time.sleep(5)