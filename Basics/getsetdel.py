class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@email.com"

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # @property
    # def first(self):
    #     return self.__first
    #
    # @first.setter
    # def first(self,first):
    #     self.__first = first
    #
    @property
    def fullname(self):
        return "{} {}".format(self.__first, self.__last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.__first = first
        self.__last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.__first = None
        self.__last = None


emp_1 = Employee('Aabid', 'Hussain')
emp_1.fullname = 'Aishwary Gautam'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# del emp_1.fullname