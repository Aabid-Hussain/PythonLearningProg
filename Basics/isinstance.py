class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last

    @classmethod
    def have_laptop(cls,laptop_input):
        if laptop_input == True:
            return "Laptop is provided"
        else:
            return "Desktop is provided"

    def __str__(self):
        return "{} has monthly pay of -->{} and email address --> " \
               "{}".format(self.fullname(),self.pay,self.email)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,
                                             self.last,
                                             self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Aabid','Hussain',50000)
emp2 = Employee('Aishwary','Gautam', 60000)

# print(emp1.have_laptop(True))
#
# print(isinstance(emp1,Employee))
#
# print(emp1.__str__())
# print(emp1.__repr__())

print(len(emp1))
print(emp1 + emp2)
print(emp1 + emp2)