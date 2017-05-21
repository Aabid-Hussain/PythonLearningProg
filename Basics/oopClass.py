class Employee:

    num_of_emps = 0  #used as Class variable
    raise_amount = 1.04 # used as instance variable

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullName(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



print(Employee.num_of_emps)

emp_1 = Employee('Aabid', 'Hussain', 50000)
emp_2 = Employee('Test', 'Bed', 60000)
emp_3 = Employee('Test3', 'Bed3', 60003)

print(Employee.num_of_emps)
print(emp_1.fullName())
