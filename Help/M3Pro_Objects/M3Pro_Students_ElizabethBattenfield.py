#M3Pro Objects
#CSC-221 M3Pro--Students Class
#Elizabeth Battenfield

class students:  #creates class 
    """Holds information on students""" 
    
    def __init__(self, idNumber, firstName, lastName, major): 
        #creates and initilizes class attributes, that every object of this class will have
        """Initialize student data"""
        
        self.idNumber = idNumber 
        self.firstName = firstName
        self.lastName = lastName
        self.major = major
        
    def __str__(self): #class objects will automatically go through this when printed
        """ string representation of the student """ 
        SPACER = '\t' #added to create a uniform space between each attribute
        text = self.idNumber + SPACER 
        text += self.firstName  + SPACER #added each attribute to same line for print ease
        text += self.lastName + SPACER #+space will make it look better
        text += self.major  + SPACER 
        
        return text #returns string containing all attributes in readable fashion
        
def main():
    
    student1 = students('47899','Susan','Meyers','Accounting') #creates objects with class attributes
    student2 = students('39119','Mark','Jones','Programmer')
    student3 = students('81774','Joy','Rogers','Engineering')      
    
    print(student1) #prints objects with class attributes in one line per object. 
    print(student2)
    print(student3)
    
if __name__ == "__main__": 
    main()
