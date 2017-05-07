
# ---------- GETTERS & SETTERS ----------
# Getters and Setters are used to protect our objects
# from assigning bad fields or for providing improved
# output

class Square(object):

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter
    @property
    def height(self):
        print("Retrieving the height")

        # Put a __ before this private field
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):

        # We protect the height from receiving a bad value
        if value.isdigit():

            # Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # This is the getter
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    aSquare = Square()

    height = raw_input("Enter height : ")
    width = raw_input("Enter width : ")

    aSquare.height = height
    aSquare.width = width

    print "Height :", aSquare.height
    print "Width :", aSquare.width

    print "The Area is :", aSquare.getArea()

main()