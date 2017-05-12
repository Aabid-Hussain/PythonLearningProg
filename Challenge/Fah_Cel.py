class TempChange(object):
    #global count

    def __init__(self,temperature=0):
        self.__temperature = temperature

    @property
    def temperature(self):
        print "Getting Temperature Value: {}".format(self.__temperature)
        return self.__temperature

    @temperature.setter
    def temperature(self,temp):
        self.__temperature = temp

    def farenhite(self,temperature):
        return ((float(9)/5) * temperature +32)

    def celcius (self, temperature):
        return ((float(5)/9)*(temperature -32))

    def __str__(self):
        return "The temperature = {} in Farenhite is =" \
               " {} and Celcius is = {}".format(self.temperature,
                                                self.farenhite(self.temperature),
                                                self.celcius(self.temperature))

def main():

    temp = TempChange(100)
    print temp
    print temp.celcius(100)
    print temp.farenhite(100)
    #print count

main()
