class Animal(object):

    def __init__(self, birthType ="Unknown", appearance = "Unknown", blooded = "Unknown"):
        self.__birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        print
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        print
        return self.__appearance

    @appearance.setter
    def appearance(self,appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        print
        return self.__blooded

    @blooded.setter
    def blooded(self,bloodedType):
        self.__blooded = bloodedType

    def __str__(self):

        return "An {} is {}, it has {}, it is {} ".format(type(self).__name__, self.birthType,
                                                         self.appearance,self.blooded)

class Mammal(Animal):

    def __init__(self,birthType = "born alive",appearance = "hairy or fur",
                  blooded = "Warm blooded", nurseYoung = True):

        Animal.__init__(self,birthType,appearance, blooded)

        self.nurseYoung = nurseYoung

    @property
    def nurseYoung(self):

        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self,nurseYoung):
        print
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return self.__str__() + " and it is {} that they nurse"\
                            "their Young".format(self.__nurseYoung)
class Reptile(Animal):

    def __init__(self,birthType = "born in an egg, born alive",appearance = "egg cell",
                  blooded = "Cold blooded"):
        Animal.__init__(self,birthType,appearance,blooded)

    def __str__(self):
        return Animal().__str__() + " and it is {} ".format(type(self).__name__)

    def SumRandom(self, *argv):
        Sum =0
        for i in argv:
            Sum +=i
        return Sum

def getbirthType(theObject):
    return "{} is {}".format(type(theObject).__name__,theObject.birthType)

def main():

    Animal1  = Animal("born alive")

    print Animal1.birthType
    print Animal1

    Mam = Mammal()
    print Mam.birthType
    print Mam.appearance
    print Mam.blooded
    print Mam.nurseYoung

    Rep = Reptile()
    print Rep.SumRandom(1,2,3,4,5)

    print getbirthType(Mam)
    print getbirthType(Rep)

main()

