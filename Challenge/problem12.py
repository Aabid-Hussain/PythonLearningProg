# --------------PROBLEM-------------
# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd.
# The surrounding function will return a list of odd
# numbers

def is_odd_number(num):
    if num % 2:
        return True
    else:
        return False

def listChange(list,func):

    oddList = []

    for number in list:
        if func(number):
            oddList.append(number)

    return oddList

newList = range(1, 100)

print listChange(newList,is_odd_number)

