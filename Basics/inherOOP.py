class Employee:
    raisedAmt = 1.10

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.Email = first + "." + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last

    def get_raised_amt(self):
        self.pay = int(self.pay * self.raisedAmt)
        return self.pay

    @classmethod
    def Increment_Salary(cls, amt):
        cls.raisedAmt = amt
        return cls.raisedAmt

    @classmethod
    def getString(cls,string):
        first, last, pay = string.split(',')
        return cls(first, last, pay)


    @staticmethod
    def Check_Working_Day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True

class Developer(Employee):

    raisedAmt = 1.50

    def __init__(self,first, last, pay, prog_lang):
        Employee.__init__(self, first,last,pay)
        #Employee.__init__(self, first, last, pay) both are correct
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self,first,last,pay,employees =None):
        #super().__init__(first,last,pay)
        Employee.__init__(self, first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):

        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('\t -->', emp.fullname())



dev_1 = Developer("Aabid","Hussain",50000,'Python')
dev_2 = Developer("Aishwary", "Gautam", 60000,'Java')


mgr_1 = Manager('sue','Smith',90000,[dev_1])

print(mgr_1.Email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emp()



# print(dev_1.Email)
# print(dev_1.prog_lang)
#

# print(help(Developer))

# print(dev_1.pay)
# dev_1.get_raised_amt()
# print(dev_1.pay)
# print(dev_2.Email)





#
#
# import datetime
#
# emp1 = Employee('A','a',1000)
#
# print(emp1.Email)
# emp12 = "Aabid,Hussain,150000"
#
# print(emp1.Email)
# emp12Obj = Employee.getString(emp12)
# print(emp12Obj.Email)
#
# today = datetime.date(2017,5,22)
#
# if Employee.Check_Working_Day(today) == True:
#     print("{} is weekday".format(today))
# else:
#     print("{} is weekend".format(today))
#
# print(Employee.Increment_Salary(1.20))
#
# print(emp1.get_raised_amt())