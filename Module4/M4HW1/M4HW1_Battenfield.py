"""
CSC-221
M4HW - Classes_inheritance
Elizabeth Battenfield
11/15/2021

exercise 10.16(Account Inheritance hierarchy) on page 426 of text book
"""



""" Checking Account and Savings Account subclasses for Account"""
from decimal import Decimal
from account import Account
        
class CheckingAccount(Account):
    """
    Checking Account class that uses Account class and costs a fee per successful transaction
    """
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.__fee = Decimal(2.50)

    def __str__(self): #gives clear description for when printing 
        return f'Checking Account:\n{self.name}   {self.balance}'
        
    def deposit(self, amount):
        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        
        self.balance += amount - self.__fee
        
        
    def withdraw(self, amount):
        # if amount is less than 0.00, raise an exception
        if amount < self.__balance + self.__fee:
            raise ValueError('Not efficient funds.')        
            
        self.balance -= amount - self.__fee
        
class SavingsAccount(Account):
    """
    Savings Account class that uses Account class and adds an interest to the account
    """
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.__rate = Decimal(0.5)        
    
    def __str__(self): #gives clear description for when printing 
        return f'Savings Account:\n{self.name}   {self.balance}'
    # inherits deposit method without redefining it.
        
    def withdraw(self, amount):
        """Withdraws specified amount from savings account."""
        #assignment says to inherit the withdraw method without redefining it, but there is no orignal withdraw method
        # if amount is less than 0.00, raise an exception
        if amount < self.balance:
            raise ValueError('Not efficient funds.')   
        
        self.balance += amount #takes balance and adds amount to it
            
        
    def calculate_interest(self):
        """Calculates the interest by multiplying the interest rate by the account balance"""
        interest = self.__rate * self.balance 
        return Decimal(interest)
    
def main():
    account1 = CheckingAccount('Bob Evans', 5000) # creates checking account object
    account2 = SavingsAccount('Cherry Smith', 30) # creates savings account object
    #prints objects 
    print(account1)    
    print(account2)
    interest = SavingsAccount.calculate_interest(account2) # calculates interest on savings account object
    account2.deposit(int(interest)) #deposits the interest into the savings account
    #prints updated object 
    print(account2)

main()