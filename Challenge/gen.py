#-----------PROBLEM----------
#Create a class that returns values from the Fibonacci
#Sequence each time next is called
#Sample Output
#Fib : 1
#Fib : 2
#Fib :3

class Fibonacci:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):

        self.a, self.b = self.b, (self.a +self.b)
        return self.a

fibo = Fibonacci()

for fib in range(10):
    print("Fib : ", next(fibo))