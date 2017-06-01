def first_func():

    def second_func():
        print("This is second function. \n")
        print("Thank you for calling {}".format(second_func.__name__))

    print("This is first function. \n")
    print("Calling second_function now")
    second_func()

first_func()

#Python allows to define func under func.
def Temp(t):

    def Cel2Faren(t):
        return (9 * t / 5 + 32)

    result = "It's " + str(Cel2Faren(t)) + "degrees!"
    return result

print(Temp(20))

#passing function within function
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("Function real name is {}".format(func.__name__))


f(g) #function is calling function



