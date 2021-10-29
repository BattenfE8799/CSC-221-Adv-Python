#calculator with doctest
#M3T2-doctest
#Elizabeth Battenfield
#CSC-221


class Calculator: #class header
""" basic calculator that adds or multiplies  """

    def __init__(self, ):
        """Initialize ."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance
        
        
    def add():
        """ addition """
        x = input("Enter first number: ")
        y = input("Enter your second number: " )
        z = x + y
        print(x," + ",y," = ",z)
        
    
    def multiply():
        x = input("Enter first number: ")
        y = input("Enter your second number: " )
        z = x * y
        print(x," * ",y," = ",z)
        
def main():
    """ main menu"""
    choice = int(input("1.add\n2.multiply"))
    if choice == 1:
        problem.add()
    else:
        problem.multiply()

if __name__ == "__main__":
    main()


        
