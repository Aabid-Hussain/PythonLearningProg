#hasattr(object,string)

class SumAll:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Sum(self):
        return self.x + self.y

def main():

    Sum1 = SumAll(10,20)
    print(Sum1.Sum())
    print(getattr(Sum1,'x'))
    print(getattr(Sum1,'y'))
    print(getattr(Sum1,'Sum'))
    print(getattr(Sum1,'z',1000))


main()