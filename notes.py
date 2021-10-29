""" Notes
"""

# CLASSES
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

#classes create a new local namespace where all its attributes are defined.
""" Attributes may be data or functions """
---''' special attributes begin and end with (__) example: __special__'''
#
# 
# SUPERCLASS: baseclass
# new class = derived class or subclass
#
# designate that the new class to be formed initially by inheriting the attributes/values and methods/functions of a previously defined base class
#
# after inheriting, customize the derived class to meet the specific needs of application
# 
# POLYMORPHISM: enables you to program in general rather than in specific. 
#-send same method call to objects possibly of many different types
#
#data classes- uses more concise notation and by autogenerating portions of the classes
#
"""CONSTRUCTOR EXPRESSION """ 
'''creates an object instance of that class. aka object that has attributes of that class'''
#--creates a new object, then initializes its data by calling the class's __init__ method.
#---does this by using argument(s) specified in parentheses. ex: newObject = className('string argument', otherArgument)
#---- account1 = Account('John Green',Decimal('50.00)) (Decimal being another class)

""" ATTRIBUTES"""
#

# ACCESSING CLASS ATTRIBUTES
#-object.attribute---outputs what value is saved there. 
#example: account1.name ouputs as 'John Green'
###as soon as we define a class, a new class object is created with the same name. 
####this object allows us to access the different attributes as well as instantiate new object of that class.
'''original class object, created when class is defined. class className ; new object is className.
   used as className.attribute or className.function...example: print(className.attribute1) or print(className.function1)'''
        
#__INIT__ METHOD--
#--each new class you create can provide an __init__ method that specifies how to initialize an object's data attributes.
#---returning a value other than None from __init__ results in a type error. (no return statement)
#-special methods have leading and trailing underscores(__) in method name

"""self."""
''' whenever an object calls its method(function), the object itself is passed as the first argument.
          example: object.function1() translates into className.function1(object)'''
#--all methods of a class must specifiy at least one parameter, usually called self.
#--self is used to access the object's attributes and other methods. 

"""CLASS DEFINITION"""
#begins with the keyword class followed by the class's name and a colon(:). also called CLASS HEADER <
#example:
#class Account:
#   """Account class for maintaining a bank account balance.""" (This is docstring of class)

class className: #class header: begins class definition 
    """ Class docstring """ #immediately following header;to read type class name and ? example className?
    
    def __init__(self, attribute1, attribute2): # this function gets called whenever a new object of this class is instantiated.
        """Initialize an object. used to initialize all the variables for the class"""  
        
        # if balance is less than 0.00, raise an exception
        if attribute2 < 0:
            raise ValueError('Initial balance must be >= to 0.') #this will terminate the __init__ method
        
        self.attribute1 = value  #dynamically adds attributes via assignments
        self.attribute2 = value2 #attributes cannot validate the values you assign them
        
        
class Account:
    """ example class: Account class for mainting a bank account balance."""
    
    def __init__(self, name, balance) #self(object) has to be the first argument 
        
        
    