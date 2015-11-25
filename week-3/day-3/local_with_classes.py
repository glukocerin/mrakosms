# def make_account():
#     return {'balance': 0}

class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):lis
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
