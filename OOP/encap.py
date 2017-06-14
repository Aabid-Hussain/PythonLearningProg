#python encapsulation(The Art of data hiding)
# public, private,(protected which has nothing to do with security
# _variable, _method

class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def Triangle_Area(self):
        return 1/2*(self.width * self.height)


class Square(Shape):

    def __init__(self, side_len):
        super(Square, self).__init__(side_len,side_len)
        self.side_len = side_len


class triangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self, width, height)


Rec = Shape(20, 30)
Squ = Square(10)
tri = triangle(20, 30)

print(Rec.area())
print(Squ.perimeter())
print(tri.Triangle_Area())

'''
class Human:

    def walk(self,name):
        print("{} can walk".format(Human.name))

class Male(Human):

    def __init__(self, name, gender):

        Human.__init__(self, name, gender)
'''