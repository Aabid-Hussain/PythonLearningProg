class Animal(object):

    def __init__(self, birthType ="Unknown", appearance = "Unknown", blooded = "Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        print ()
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        print ()
        return self.__appearance

    @appearance.setter
    def appearance(self,appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        print ()
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
        print()
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self,nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return Animal().__str__() + " and it is {} that they nurse"\
                            "their Young".format(self.nurseYoung)

def main():

    Animal1  = Animal("deer")

    print Animal1.birthType
    print Animal1

main()

