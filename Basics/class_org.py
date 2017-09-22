class Shape:

    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value>=0:
            self.__width = value

        else:
            print("Please enter positive integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value

        else:
            print("Please enter positive integer")

    def getArea(self):
        return self.__width * self.__height

class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self, width = 1, height = 1)
        self.side = side

    def getArea(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length = 1 , base = 1):
        Shape.__init__(self,width=1, height=1)
        self.length = length
        self.base = base

obj = Square(12)
objRect = Rectangle(10,20)
objRect1 = Rectangle()

print(obj.getArea())
print(objRect.getArea())
print(objRect1.getArea())









