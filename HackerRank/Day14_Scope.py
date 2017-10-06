class Difference:
    def __init__(self, a):
        self.__elements = a
        self.__maximumDifference = 0

    def computeDifference(self):
        maxi_value = abs(min(self.__elements) - max(self.__elements))
        self.maximumDifference = maxi_value


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)