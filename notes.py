""" Notes
"""

# classes
# Everything in python is an object
# objects are built from classes
# building a new object from even a large class is simple, you typically write one statment
# 
# classes, objects, inheritance, and polymorphism
# oop makes it easier for you to design, implement, test, debug, and update apps
# object-based programming primarily create/use objects of exisiting classes
# 
# classes are new data types
# most applications you'll bulid for your own use will commonly use either no custom classes or just a few
# 
# new classes can be formed through inheritance and composition from classes
# 
# superclass: baseclass
# new class = derived class or subclass
#
# designate that the new class to be formed initially by inheriting the attributes/values and methods/functions of a previously defined base class
#
# after inheriting, customize the derived class to meet the specific needs of application
# 
# Polymorphism: enables you to program in general rather than in specific. 
#-send same method call to objects possibly of many different types
#
#data classes- uses more concise notation and by autogenerating portions of the classes
#
# CONSTRUCTOR EXPRESSION- 
#--creates a new object, then initializes its data by calling the class's __init__ method.
#
#__INIT__ METHOD--
#--each new class you create can provide an __init__ method that specifies how to initialize an object's data attributes.
#---returning a value other than None from __init__ results in a type error. (no return statement)
#-special methods have leading and trailing underscores(__) in method name

#SELF
#--all methods of a class must specifiy at least one parameter, usually called self.
#--self is used to access the object's attributes and other methods. 
class className: #class header: begins class definition 
    """ Class docstring """ #immediately following header;to read type class name and ? example className?
    
    def __init__(self, attribute1, attribute2):
        """Initialize an Account object."""
        
        # if balance is less than 0.00, raise an exception
        if attribute2 < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.') #this will terminate the __init__ method
        
        self.attribute1 = value  #dynamically adds attributes via assignments
        self.attribute2 = value2 #attributes cannot validate the values you assign them
        
        
    