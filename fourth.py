class BankAccount: #bank class
    def __init__(self, account_holder, account_number, balance=0.0):#constructer balance is default vale = 0.0
        self.account_holder = account_holder#assign values to members
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):#deposit method
        self.balance += amount#add it to balance
        print(f"{self.account_holder} Deposited {amount} $")#print depositing event
        
    def withdraw(self, amount):#withdraw method
        if self.balance >= amount:#check user have enough balance
            self.balance -= amount#discount it from user balance
            print(f"{self.account_holder} Withdrew {amount} $")#print event to user
        else:
            print("You don't have enough funds to withdraw.")#print insufficient balance error
    
    def get_balance(self):# print method
         print(f" Current balance is: {self.balance} $.")
         
test = BankAccount("yara", "1234")#create object
test.deposit(1000)
test.withdraw(500)
test.get_balance()#ptint balance


class SavingsAccount(BankAccount):#inheritance
    def __init__(self, account_holder, account_number, interest_rate, balance=0.0):#constructor
        super().__init__(account_holder, account_number, balance)#call parent constructor
        self.interest_rate = interest_rate#assign value
        
    def apply_interest(self):#apply interest method
         interest = self.balance * self.interest_rate
         self.deposit(interest)
         
    def get_balance(self):#override print method
         print(f" Current balance is: {self.balance} $ and current rate is {self.interest_rate} .")
         
saving = SavingsAccount("yara", "123456789", 20) #test class
saving.deposit(1000)
saving.apply_interest()
saving.get_balance()