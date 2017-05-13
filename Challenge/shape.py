class Canvas(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' '] * width for i in range(height)]

    def setpixel(self, row, col):
        self.data[row][col] = '*'

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print "\n".join(["".join(row) for row in self.data])

class Shape(object):
    def paint(self, canvas): pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def hline(self, x, y, w):
        pass

    def vline(self, x, y, h):
        pass

    def paint(self, canvas):
        hline(self.x, self.y, self.w)
        hline(self.x, self.y + self.h, self.w)
        vline(self.x, self.y, self.h)
        vline(self.x + self.w, self.y, self.h)

class Square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)

class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def paint(self, canvas):
        for s in self.shapes:
            s.paint(canvas)

def main():

    a = Canvas(10,20)

    print a

main()