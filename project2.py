#Banking System through OOPS
#account create
#deposit
#withdraw 
#balance check

class Bank_Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no=acc_no
        self.name=name
        self.__balance=balance     #protected
    
    def deposit(self,amount):
        if amount<0:
            print("invalid amount for deposit")
        else:
            self.balance=self.balance + amount

    def withdrawAmount(self, amount):
        if amount>self.balance:
            print("insufficient amount")
        else:
            self.balance-=amount

    def getBalance(self):
        return self.__balance

class Saving_Account(Bank_Account):
    def __init__(self, acc_no, name, balance):
        self.min_balance=500
        if(balance>self.min_balance):
            super().__init__(acc_no, name, balance)
    
    def withdrawAmount(self, amount):
        self.getBalance()
        if self.balance-amount>= self.min_balance:
            self.balance-=amount
            print(f"Saving withdraw {amount} New balance is {self.balance}")
        else:
            print(f"Cant withdraw, please manage the min balance {self.min_balance}")

class Current_Account:
        def __init__(self, acc_no1, name1, balance1):
            self.acc_no1=acc_no1
            self.name1=name1
            self.balance1=balance1

        def withdraw(self, amount):
            if self.balance1-amount>= self.balance1:
                self.balance1-=amount
                print(f"Saving withdraw {amount} New balance is {self.balance}")
            else:
                print(f"Cant withdraw, please manage the min balance {self.min_balance}")

s1=Saving_Account(23, "pri", 9000)
print(s1.getBalance())
s1.withdrawAmount(600)
