'''

balance = 0

def deposit(amt):
    global balance
    balance += amt
    return amt

def withdraw(amt):
    global balance
    balance -= amt
    return amt

print("Customer Deposit: {}".format(deposit(
                        int(input("Enter Deposit Amt: ")))))
print("Current Balance: {}".format(balance))
print("Customer Withdraw: {}".format(withdraw
                    (int(input("Enter Withdraw Amt: ")))))
print("Current Balance: {}".format(balance))


def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = make_account()
print(deposit(a,1000))
print(withdraw(a,100))
b = make_account()
print(deposit(b,1000))
'''


class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())