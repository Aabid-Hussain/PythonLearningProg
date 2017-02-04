'''Define a class which has at least two methods:getString: to get a string from console input
printString: to print the string in upper case.Also please include simple test function
to test the class methods.'''

class objclass:
    def __init__(self): #used for initialization and to construct parameter/s
        self.s = ""
    def getString(self):
        self.s = raw_input()
    def printString(self):
        print self.s.upper()


strObj = objclass() #initialized class
strObj.getString() #methods are called using object
strObj.printString()


