# Calculate the tip as per user input
from __future__ import print_function

bill= raw_input("What is the bill? ")
tip = input("What is the tip percentage? ")

if bill.startswith('$'):

    bill = int(bill.replace('$',''))


tip_cal_amt = (float(bill)*tip)/100

print("The tip is ${0:.2f}".format(tip_cal_amt))
print("The total is ${0:.2f}".format(float(bill)+tip_cal_amt))


