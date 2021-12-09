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
        """ adds to numbers given """
        """
        >>> Calculator.add(x,2,3)
        '2 + 3 = 5'
        """
        z = x + y
        text = str(x) + ' + '
        text += str(y) + ' = '
        text += str(z)
        return text
        
    
    def multiply(self,x,y):
        """ multiplys two numbers given """
        """
        >>> Calculator.multiply(x,2,3)
        '2 * 3 = 6'
        """
        z = x * y
        text = str(x) + ' * '
        text += str(y) + ' = '
        text += str(z)
        return text
        
def main():

    """ main menu"""
    """
    >>>2+3
    '2 + 3 = 5'
    
    >>>2*3
    '2 * 3 = 6'
    """

    again = 1
    while (again == True):
        equation = input("Enter your addion(+) or multiplication(*) equation. ")
        if "+" in equation:
            prob = equation.split("+")
            x = int(prob[0])
            y = int(prob[1])
            solved = Calculator(x, y)
            answer = solved.add(x,y)
            
        elif "*" in equation:
            prob = equation.split("*")
            x = int(prob[0])
            y = int(prob[1])
            solved = Calculator(x, y)
            answer = solved.multiply(x, y)
        
        print(answer)
            
        
        choice = input("\nDo you want to do another? ")
        if choice == 'y':
            again = True
        elif choice == 'n':
            break
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()


        
