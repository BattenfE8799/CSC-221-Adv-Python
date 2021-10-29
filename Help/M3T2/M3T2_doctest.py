#calculator with doctest
#M3T2-doctest
#Elizabeth Battenfield
#CSC-221

#note from notes: 

class Calculator: #class header
    """ basic calculator that adds or multiplies  """

    def __init__(self, x, y):
        """Initialize ."""
        self.x = x
        self.y = y
                
    def add(self, x, y):
        """ addition """
        x = input("Enter first number: ")
        y = input("Enter your second number: " )
        z = x + y
        print(x," + ",y," = ",z)
        
    
    def multiply(self):
        x = input("Enter first number: ")
        y = input("Enter your second number: " )
        z = x * y
        print(x," * ",y," = ",z)
        
def main():
    """ main menu"""
    print("")
    equation = input("Enter your addion(+) or multiplication(*) equation.")
    prob = 
    if choice == 1:
        problem.add()
    else:
        problem.multiply()

if __name__ == "__main__":
    main()


        
