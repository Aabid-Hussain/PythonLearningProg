'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

class InputOutputClass:

    def __init__(self):
        self.inputData= ""

    def getString(self):
       self.inputData = raw_input("Enter your String: ")

    def printString(self):
        print "UpperCase: {} ".format(self.inputData.upper())

def main():
    StrObj = InputOutputClass()
    StrObj.getString()
    StrObj.printString()

main()
