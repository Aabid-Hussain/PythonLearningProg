class Employee:

    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def raise_amt_output(self):
        raise_amt = self.raise_amt
        return raise_amt

    @classmethod #
    def get_raise_amt(cls,amt):
        cls.raise_amt = amt
        return cls.raise_amt

    # used to create instances of a class by parsing string.
    @classmethod
    def _get_string(cls,class_str):
        first,last,pay = class_str.split('-')
        return cls(first,last,pay)





emp1 = Employee('A',"a","10")
emp2 = Employee('B',"b","100")
emp3 = Employee('C',"c","1000")

emp1_str = 'aabid-hussain-1500'

# print(emp3.first,emp3.last,emp3.pay,emp3.email)

print(Employee._get_string(emp1_str).email)
print(Employee._get_string(emp1_str).first)
print(Employee._get_string(emp1_str).last)
print(Employee._get_string(emp1_str).pay)
#
# print(Employee.get_raise_amt(1.05))
#
# print(emp1.raise_amt_output())
# print(emp2.raise_amt_output())
# print(emp3.raise_amt_output())
# # print(emp2.raise_amt_output())
# # print(emp3.raise_amt_output())