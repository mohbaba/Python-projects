class Account:
    
    def __init__(self, account_no, account_balance=0):
        
        self.account_no = account_no
        self.account_balance = account_balance
        

    
    def credit(self,amount):
        self.account_balance += amount
        print (self.account_balance)
        
    def debit(self,amount):
        if self.account_balance < amount:
            print ('Insufficient Funds!')
        else:
            self.account_balance-= amount
            print (self.account_balance)
    
class SavingsAccount(Account):
    
    def __init__(self, account_no , account_balance=0):
        super().__init__(account_no ,account_balance)
        
    

class CurrentAccount(Account):
    pass


savings_account = SavingsAccount(4567)

savings_account.credit(8000)
savings_account.debit(2000)