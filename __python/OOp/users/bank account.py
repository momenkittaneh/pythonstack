class BankAccount:
    def __init__(self,int_rate,balance):
        int_rate = int_rate
        balance = balance
    def deposit(self,amount):
        balance += amount
    def withdraw(self,amount):
        if amount<balance:
            balance -= amount
        else:
            print(f"Insufficient funds: Charging a ${amount} fee and deduct ${balance}")
    def yield_interest(self):
        if balance>0:
            balance += balance * int_rate

bank1= BankAccount(10,1000)
bank2= BankAccount(5,2000)

bank1.deposit(1000)
bank1.deposit(200)
bank1.yield_interest()
bank1.display_account_info()