class user:
    def __init__(self, name, email_address,account_balance):
            self.name = name			
            self.email = email_address		
            self.account_balance = account_balance		
    def make_deposit(self, amount):	
            self.account_balance += amount
            return self
    def make_withdrawal(self, amount):
        if amount<self.account_balance:
            self.account_balance-=amount
            return self

        else:
            return self
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self
    
    

kristeen=user("kristeen","kris@mail.com",1000)
momen=user("momen","momen@mail.com",2000)

eli=user("eli","eli@mail.com",2000)

kristeen.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
momen.make_deposit(1000).make_deposit(2000).make_deposit(300).make_withdrawal(1500).display_user_balance()
eli.make_deposit(900).make_deposit(2400).make_deposit(600).make_withdrawal(1500).display_user_balance()