"""
CSC-221
M4HW - Classes_inheritance
Elizabeth Battenfield
11/15/2021

exercise 10.16(Account Inheritance hierarchy) on page 426 of text book
"""

from account import Account # import the account class from the account.py
from decimal import Decimal # import decimal
#create two subclasses
#checking account dont earn interest and charge a fee per transaction
class CheckingAccount(Account):
    """
    Checking Account subclass that charges a fee per successful transaction
    """
    def __init__(self, name, balance):
        """
        Initializes Checking Account attributes
        """
        super().__init__(name, balance)
        self.Rate = Decimal(2.50)
    
    #set balance
    def get_balance(self):
        return Account.balance 
    
    #get balance
    def set_balance(self, balance):
        """
        updates the balance
        """
        Account._balance = balance #invokes base-class account to update the account balance
        
    #withdraw that overrides the account class withdraw
    def withdraw(self, amount): 
        """withdraw money from the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        # if amount is more than the balance plus rate, raise an exception
        if amount > self.balance + self.Rate:
            raise ValueError('not enough funds in account.')

        self.balance -= amount  #subtracts amount from balance for new balance       
    
    #deposit that overrides the account class deposit method
    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount #adds amount to balance for new balance
        
    

#savings account can earn interest on the money they hold
# should include data attribute indicating the interest rate.

class SavingsAccount(Account):
    """
    Savings Account subclass that adds a calcualted interest to the account balance
    """
    def __init__(self, name, balance):
        """
        Initializes Savings Account attributes
        """
        super().__init__(name, balance)
        self.Rate = Decimal(0.5)
    
    #set balance
    def get_balance(self):
        return super().balance 
    
    #get balance
    def setBalance(self, balance):
        """
        updates the balance
        """
        super().balance = balance #invokes base-class account to update the account balance
        
    #withdraw that overrides the account class withdraw
    def withdraw(self, amount): 
        """withdraw money from the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        # if amount is more than the balance plus rate, raise an exception
        if amount > self.balance + self.Rate:
            raise ValueError('not enough funds in account.')

        self.balance -= amount  #subtracts amount from balance for new balance       
        setBalance(self.balance)
    
    #deposit that overrides the account class deposit method
    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount #adds amount to balance for new balance
        setBalance(balance)
    
    #^^ should inherit methods deposit and withdrawl without redefining them
    
    def calculate_interest(self, balance, Rate):
        #should return the Decimal result of multiplying the interest rate by the account balance
        #should pass the returned interest amount to the objects deposit method
        """
        calculates the interest that will be added to the balance
        """
    
account1 = Account('Jeorge',500)
