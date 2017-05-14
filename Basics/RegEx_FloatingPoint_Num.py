'''Task
You are given a string .
Your task is to verify that  is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
Number can start with +, - or . symbol.
Number must have exactly one . symbol.
Number must not give any exceptions when converted using .
Input Format
The first line contains an integer , the number of test cases.
The next  line(s) contains a string .
Constraints
Output Format
Output True or False for each test case.
Sample Input
4 4.0O0 -1.00 +4.54
SomeRandomStuff
Sample Output
False
True
True
False'''

import re

n =input("!!!Enter the value 0 to quite!!!\n")
while n !=0:

    randStr = raw_input("Enter the Sample Output")
    RegEx = r"^[+-.]?*\.\d+"
    matches = re.search(RegEx,randStr)
    print matches.group()
