class Geom(object):

    def __init__(self,base="0",height="0"):
        self.__base = base
        self.__height = height

    @property
    def base(self):
        print "Retrieving base : "
        return self.__base

    @base.setter
    def base(self,base):
        self.__base = base

    @property
    def height(self):
        print "Retrieving height: "
        return self.__height

    @height.setter
    def height(self,height):
        self.__height =height

class Square(Geom):

    def __init__(self,base="0",height = "0",side=True):

        Geom.__init__(self,base,height)
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self,side):
        self.__side = side

    def __str__(self):
        return "{} is equal to {} and it is {}".format(self.base,self.height,
                                    type(self).__name__)

class Rectangle(Geom):
    def __init__(self, base="0", height="0", side=False):
        Geom.__init__(self, base, height)
        self.side =side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self,side):
        self.__side = side

    def __str__(self):
        return "{} is not equal to {} and it is {}".format(self.base, self.height,
                                                       type(self).__name__)

def main():

    Geo1 = Geom("10","20")

    aSquare = Square()
    aRectangle = Rectangle()
    print Geo1.height
    print Geo1.base
    print aRectangle
    print aSquare

main()