class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")
    
    def statement(self):
        print(f"Account Balance: {self.balance}")

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)
    def __str__(self):
        return f"{self.name}'s Current Account, Balance: {self.balance}"

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
    def __str__(self):
        return f"{self.name}'s Savings Account, Balance: {self.balance}"

x = Current("Benny", 1000)
y = Savings("Benny", 2000)
x.deposit(500)
x.statement()
x.withdrawal(2000)
x.statement()
x.withdrawal(500)
x.statement()
x.withdrawal(1)
x.statement()
print(x)
y.statement()
y.withdrawal(1500)
y.statement()
y.withdrawal(500)
y.statement()
y.withdrawal(1)
y.statement()
print(y)


# output
"""

Account Balance: 1500
Account Balance: -500
Account Balance: -1000
Sorry, not enough funds!
Account Balance: -1000
Benny's Current Account, Balance: -1000
Account Balance: 2000
Account Balance: 500
Account Balance: 0
Sorry, not enough funds!
Account Balance: 0
Benny's Savings Account, Balance: 0

"""