# -*- coding: utf-8 -*-
"""
Notes 
v 1.1 added notes on dataclasses (frorm https://www.youtube.com/watch?v=vBH6GRJ1REM&t=86s )
"""


class ManualComment:
    """ Data class """
    
    def __init__(self, id: int, text: str):
        self.__id: int = id       #makes id an int type
        self.__text: str = text   #makes text a string type
    
    @property #makes id immutable, readable not writable
    def id(self): #calls this instead of above
        return self.__id
    
    @property #makes id immutable,  readable not writable
    def text(self):
        return self.__text
    
    def __str__(self):
        """method defines behavoir when you pass class instance through this.
           returns a string representation of an object that is human readable.
           calls __repr__ internally by default."""
          
        return f'({self.id},{self.text})'
    
    def __repr__(self):
        """ dunder method defines behavor when you pass an instance of a class to the repr().
            it returns the string representation of an object. 
            This is for machine readable """
        return f'ManualComment("{self.id}",{self.text})'
    
    def __eq__(self, other):
        """ dunder method. automatically called when you use the == operator to compare instances of a class.
        result = self.__eq__(other).
        by default,  the 'is' method is used if not providing specific implimentation for this method.
        USED to DEFINE the equality logic for comparing two objects using the (==) operator.
        """
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)  #checks to see if object is of the same class and equals them if so
        #if isinstance(other, ManualComment): #checks to see if object is an instance of the class before accessing an attribute to check if equall to
            #return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented  #if not equal they it uses the 'is' method


    def __ne__(self, other):
        """Not Equals dunder method:
            NEED MORE INFO"""
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
        
    def __hash__(self):
        """accepts an object and returns the hash value as an integer. 
           By default, the hash uses the objects identity and the eq returns true if two obejcts are the same. To override this implement the eq and hash methods.
           with eq implemented hash is set to None
           allows class instances to be used in a mapping type (ie dictionary keys or list elements)
           ^ if eq is overwritten
           use propery to make class attributes immutable
        """
        #return hash(self.id)
        return hash((self.__class__, self.id, self.text))
    
        
    def __lt__(self, other):
        """less than dunder method:
            used if sorting class instances. describes the less than operator in python.
        """
        
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented
    #def __lt__(self, other):
    # in1=self.ft*12+self.inch
    # in2=other.ft*12+other.inch
    # if in1<in2:
    #   return "first object smaller than other"
    # else:
    #   return "first object not smaller than other"
    
    
    def __gt__(self, other):
        """greater than dunder method:
            used if sorting class instances. describes the greater than operator in python.
        """
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented
      
        # in1=self.ft*12+self.inch
        # in2=other.ft*12+other.inch
        # if in1<in2:
        #     return "first object greater than other"
        # else:
        #     return "first object not greater than other"
   
    def __ge__(self, other):
        """greater than equal to dunder method:
            used if sorting class instances. describes the greater than equal to operator in python.
        """
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented
       
    pass

#checks the __init__ method
person = ManualComment(20001, "John")
#checks the __reper__ method
print("repr: ", repr(person))
print("str: ", person)

#checks the __eq__ method
person2 = ManualComment(30001, "Mary")
print("eq: ", person == person2) #should turn true

