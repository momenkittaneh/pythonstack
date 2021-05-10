class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<balance:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a ${amount} fee and deduct ${balance}")
    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance * self.int_rate
    def display_account_info(self):
        print(f"account balance= {self.balance} and the benfit= {self.int_rate}")

bank1= BankAccount(10,1000)
bank2= BankAccount(5,2000)

bank1.deposit(1000)
bank1.deposit(200)
bank1.yield_interest()
bank1.display_account_info()