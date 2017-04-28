class Human:
    def __init__(self):
        #defining the properties of the class using __init__ function
        self.name = raw_input("Enter the name of the Human:")
        self.occupation = raw_input("Enter the occupation of the Human:")

    def do_work(self):
        #defining the method of the class
        if self.occupation == " tennis player":
            print(self.name + " plays tennis")
        elif self.occupation == " actor":
            print (self.name + " shoots film")

    def speaks(self):
        #defining the method of the class
        print(self.name+ " Says how are you?")

tom = Human()
tom.do_work()
tom.speaks()

