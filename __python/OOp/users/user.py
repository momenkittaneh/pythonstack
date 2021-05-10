class user:
    def __init__(self, name, email_address,account_balance):
            self.name = name			
            self.email = email_address		
            self.account_balance = account_balance		
    def make_deposit(self, amount):	
            self.account_balance += amount
    def make_withdrawal(self, amount):
        if amount<self.account_balance:
            self.account_balance-=amount
            return True
        else:
            return False
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        trans = self.make_withdrawal(amount)
        if trans == True:
            other_user.make_deposit(amount)
    

kristeen=user("kristeen","kris@mail.com",1000)
momen=user("momen","momen@mail.com",2000)

eli=user("eli","eli@mail.com",2000)

kristeen.make_deposit(1000)
kristeen.make_deposit(200)
kristeen.make_deposit(800)
kristeen.make_withdrawal(200)
kristeen.display_user_balance()
momen.make_deposit(100)
momen.make_deposit(900)
momen.make_withdrawal(100)
momen.make_withdrawal(1000)
momen.display_user_balance()
eli.make_deposit(200)
eli.display_user_balance()
eli.make_withdrawal(1000)
eli.make_withdrawal(1000)
eli.display_user_balance()
kristeen.transfer_money(eli,200)
kristeen.display_user_balance()
eli.display_user_balance()