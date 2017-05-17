class Square(object):

    def __init__(self, height="0", width = "0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving Height value: ")

        return self.__height
    @height.setter
    def height(self,value):

        if value.isdigit():
            self.__height =value
        else:
            print("Please enter integer\n")

    @property
    def width(self):

            print("Retrieving Width value: ")

            return self.__width
    @width.setter
    def width(self,value):

        if value.isdigit():

            self.__width = value
        else:
            print( "Please enter integer \n")

    def getArea(self):

        return int(self.__height) * int(self.__width)

def main():

    aSquare = Square()

    height = input("Height: ")
    width = input("Width: ")

    aSquare.height = height
    aSquare.width = width

    print (aSquare.height)
    print (aSquare.width)

    print("Area : ", aSquare.getArea())



main()

