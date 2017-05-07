#define a class

class Rectangle(object):

    def __init__(self, base = "0", height = "0"):

        self.base = base
        self.height = base

    @property
    def base(self):

        print "Retrieving the base value: "
        return self.__base

    @base.setter
    def base(self, value):

        if value.isdigit():
            self.__base = value

        else:
            print "Please enter number\n"

    @property
    def height(self):

        print "Retrieving height value: "

        return self.__height

    @height.setter
    def height(self,value):

        if value.isdigit():
            self.__height = value

        else:

            print "Please enter number\n"

    def getArea(self):

        if int(self.__base) == int(self.__height) :

            print "Area of Square: "
            return int(self.__base) * int(self.__height)
        else:

            print "Area of Rectangle: "
            return int(self.__base) * int(self.__height)

def main():

    aRectangle = Rectangle()

    shortSide = raw_input("Enter the base: ")
    longSide = raw_input("Enter the Height: ")

    aRectangle.base = shortSide
    aRectangle.height = longSide

    print aRectangle.base, "\n", aRectangle.height

    print aRectangle.getArea()


main()


