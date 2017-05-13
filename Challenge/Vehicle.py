'''
class Vehicle fields are name and color
use getter and setter

Class Car inherit from Vehicle and has model in it, use getter and setter and method getDescription()
 
Car("Ford Mustang", "red", "GT350")
'''

class Vehicle(object):
    def __init__(self,name="Unknown", color = "Unknown"):
        self.name = name
        self.color = color

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


    def __str__(self):
        return "This {} is {} with {} color".format(type(self).__name__,
                                                    self.name,
                                                    self.color)

class Car(Vehicle):
    def __init__(self,name ="Ford Mustang",color = "red",model="Unknown"):
        Vehicle.__init__(self,name,color)

        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self,model):
        self.__model = model

    def __str__(self):
        return super(Car, self).__str__() + " and mode is {}".format(
                                            self.model)


def main():

    car1 = Vehicle("Ford Mustang", "red")
    print car1
    print car1.name
    print car1.color

    car2 = Car("swift", "black", "SWT350")
    print car2
    print car2.name
    print car2.color
    print car2.model


main()