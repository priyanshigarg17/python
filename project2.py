#Banking System through OOPS
#account create
#deposit
#withdraw 
#balance check

# class Bank_Account:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no=acc_no
#         self.name=name
#         self.__balance=balance     #private
    
#     def deposit(self,amount):
#         if amount<0:
#             print("invalid amount for deposit")
#         else:
#             self.__balance=self.__balance + amount

#     def withdrawAmount(self, amount):
#         if amount>self.__balance:
#             print("insufficient amount")
#         else:
#             self.__balance-=amount
 
#     @property    #getter
#     def getBalance(self):
#         return self.__balance
    
#     @getBalance.setter           #setter
#     def getBalance(self):
#         return self.__balance

# class Saving_Account(Bank_Account):
#     def __init__(self, acc_no, name, balance):
#         self.min_balance=500
#         if(balance>self.min_balance):
#             super().__init__(acc_no, name, balance)
    
#     def withdrawAmount(self, amount):
#         new_balance=self.getBalance
#         if new_balance-amount>= self.min_balance:
#             self.getBalance=new_balance-amount
#             print(f"Saving withdraw {amount} New balance is {new_balance}")
#         else:
#             print(f"Cant withdraw, please manage the min balance {self.min_balance}")

# class Current_Account(Bank_Account):
#         def __init__(self, acc_no, name, balance):
#            super().__init__(acc_no, name, balance)

#         def withdraw(self, amount):
#              super().withdrawAmount(amount)


import mysql.connector

# DB Connection Setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql17122003",  # <-- change this
    database="bank_system"
)
cursor = db.cursor()

class Bank_Account:
    def __init__(self, acc_no, name, balance, account_type="Generic"):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance
        self.account_type = account_type
        self.save_to_db()

    def save_to_db(self):
        cursor.execute("REPLACE INTO accounts (acc_no, name, balance, account_type) VALUES (%s, %s, %s, %s)",
                       (self.acc_no, self.name, self.__balance, self.account_type))
        db.commit()

    def deposit(self, amount):
        if amount < 0:
            print("Invalid amount for deposit")
        else:
            self.__balance += amount
            self.save_to_db()

    def withdrawAmount(self, amount):
        if amount > self.__balance:
            print("Insufficient amount")
        else:
            self.__balance -= amount
            self.save_to_db()

    @property
    def getBalance(self):
        return self.__balance

    @getBalance.setter
    def getBalance(self, value):
        self.__balance = value
        self.save_to_db()

class Saving_Account(Bank_Account):
    def __init__(self, acc_no, name, balance):
        self.min_balance = 500
        if balance > self.min_balance:
            super().__init__(acc_no, name, balance, account_type="Saving")
        else:
            print("Balance should be more than minimum balance")

    def withdrawAmount(self, amount):
        new_balance = self.getBalance
        if new_balance - amount >= self.min_balance:
            self.getBalance = new_balance - amount
            print(f"Saving withdraw {amount}. New balance is {self.getBalance}")
        else:
            print(f"Cannot withdraw, please maintain the minimum balance {self.min_balance}")

class Current_Account(Bank_Account):
    def __init__(self, acc_no, name, balance):
        super().__init__(acc_no, name, balance, account_type="Current")

    def withdraw(self, amount):
        super().withdrawAmount(amount)

# Create accounts
s1 = Saving_Account(101, "Priya", 2000)
s1.deposit(500)
s1.withdrawAmount(1000)

c1 = Current_Account(201, "Ravi", 3000)
c1.deposit(200)
c1.withdraw(500)


