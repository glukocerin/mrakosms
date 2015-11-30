class BankAccount:
    def __init__(self, name, balance):
        if type(name) != str:
            raise Exception('plese type a string')
        self.name = name
        if type(balance) != int:
            raise Exception('please type a number')
        self.balance = balance

    def pay(self, amount):
        if amount > self.balance:
            print('You haven\'t enough money. Your balance is: ', self.balance)
        else:
            self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def print_balance(self):
        print(self.name + '\'s balance:')
        print(self.balance)

    def transfer(self, name_to, amount):
        self.pay(amount)
        name_to.receive(amount)



akos = BankAccount('Akos', 10000)
ati = BankAccount('Attila', 12000)
tojas = BankAccount('Tojas', 100000)

#
# tojas.transfer(akos, 40000)
