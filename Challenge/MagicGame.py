import random
import math


# warrior & Battle Class
class Warrior(object):

    def __init__(self, name="warrior", health=0, attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax

    def attack(self):
        atkAmt = self.attackMax * (random.random() + 0.5)

        return atkAmt


    def block(self):
        blockAmt = self.blockMax * (random.random() + 0.5)

        return blockAmt
'''
    @property
    def name(self):
        print "Retrieving Name of Warrior: "
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def health(self):
        print "Retrieving Health of Warrior"
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def attackMax(self):
        print "Retrieving attackMax of Warrior"
        return self.__attackMax

    @attackMax.setter
    def attackMax(self, attackMax):
        self.__attackMax = attackMax

    @property
    def blockMax(self):
        print "Retrieving blockMax of Warrior"
        return self.__blockMax

    @blockMax.setter
    def blockMax(self, blockMax):
        self.__blockMax = blockMax  '''




class Battle(object):
    def startFight(self, warrior1, warrior2):

        while True:

            if self.getAttkResult(warrior1, warrior2) == "Game Over":
                print "Game Over"
                break

            if self.getAttkResult(warrior2, warrior1) == "Game Over":
                print "Game Over"
                break

    @staticmethod
    def getAttkResult(warriorA, warriorB):

        warriorAAttkAmt = warriorA.attack()

        warriorBBlkAmt = warriorB.block()

        damage2warriorB = math.ceil(warriorAAttkAmt - warriorBBlkAmt)

        warriorBHealth = warriorB.health - damage2warriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2warriorB))

        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))

        if warriorBHealth <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))

            return "Game Over"

        else:
            return "Fight Again"


def main():
    # Create 2 Warriors
    Aabid = Warrior("Aabid", 50, 20, 10)
    Hussain = Warrior("Hussain", 50, 20, 10)

    # Create Battle object
    battle = Battle()

    # Initiate Battle
    battle.startFight(Aabid, Hussain)


main()
