'''
Write a program that computes the net amount of a bank account based a transaction log from 
console input. The transaction log format is shown as following:

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

balance = 0
while True:
    inputData = input()
    if not inputData:
        break
    s = inputData.split(' ')
    D_WKeys = s[0]
    value = int(s[1])
    if D_WKeys == 'D':
        balance += value
    elif D_WKeys == 'W':
        balance -= value
    else:

        pass


print("Remaining Balance: {}".format(balance))



