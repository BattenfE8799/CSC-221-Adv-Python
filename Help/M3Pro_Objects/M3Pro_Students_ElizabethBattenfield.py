#M3Pro Objects
#CSC-221 M3Pro--Students Class
#Elizabeth Battenfield

class students: 
    """Holds information on students""" 
    
    def __init__(self, idNumber, firstName, lastName, major):
        """Initialize student data"""
        
        self.idNumber = idNumber 
        self.firstName = firstName
        self.lastName = lastName
        self.major = major
        
    def __str__(self):
        """ string representation of the student """
        SPACER = '\t'
        text = self.idNumber + SPACER
        text += self.firstName  + SPACER
        text += self.lastName + SPACER
        text += self.major  + SPACER
        
        return text
        
def main():
    
    student1 = students('47899','Susan','Meyers','Accounting')
    student2 = students('39119','Mark','Jones','Programmer')
    student3 = students('81774','Joy','Rogers','Engineering')      
    
    print(student1)
    print(student2)
    print(student3)
    
if __name__ == "__main__":
    main()
