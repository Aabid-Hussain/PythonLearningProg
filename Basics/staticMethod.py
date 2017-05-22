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

    #used to create method which doesn't take either self or class.
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

import datetime

my_date = datetime.date(2017,5,21)
print(Employee.is_workday((my_date)))
