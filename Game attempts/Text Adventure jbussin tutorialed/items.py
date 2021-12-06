"""
module for items class 
"""
"""
NOtes:
    subclass weapons with superclass consumable
    
"""

class Item():
    """ The base class for all items"""
    
    def __init__(self, name, description, value, weight, can_pickup, can_drop):
        """ attributes for all items to have """ 
        # ^^ constructor that is called whenever a new object is created 
        # initializes all attributes for the class
        # sets the attribute as the object/variable that was passed as a parameter
        self.__name = name      # I am using __ before each attribute to show its different from the local variables for less confusion                
        self.__description = description
        self.__value = value
        self.__weight = weight
        
        # flags for items
        self.__can_pickup = True
        self.__can_drop = True
        
    def __str__(self): 
        # ^^ allows the ability to print an object and see useful information
        # returns string of information about the object that the player can understand
        return "{}\n=====\n{}\nValue: {}\nWeight: {}\n".format(self.name, self.description, self.value, self.weight)

class Consumable(Item):
    """ class that creates consumable items"""
    
    def __init__(self, name, description, value, weight, can_pickup, can_drop, num_uses):
        super().__init__(name, description, value, weight, can_pickup = True, can_drop = True) #connects to superclass Item
        self.__num_uses = num_uses      #number of times the item can be used
    
    def set_uses(self, uses):
        """sets the number of uses, so if you drink a potion, it lowers the number of uses"""
        if uses <= 0:
            self.remove_consumable()
        elif uses < self.__num_uses:
            self.__num_uses == uses 
            
    def get_uses(self):
        """gets the number of uses left for item"""
        return self.__num_uses
    
    def remove_consumable(self):
        """remove consumable item from existance if used up"""
        return "TODO"
    
    
        

class Door(Item):
    """Class that creates doors, unlocked and locked can also be used with container class"""
    
    def __init__(self, name, description, value, weight, can_pickup, can_drop, unlock, lock, key_needed):
        super().__init__(name, description, value = -1, weight = -1, can_pickup = False, can_drop = False)
        #gives negative values to value, weight, can_pickup, and can_drop so that none of these apply to a door. 
        
        self.__lock = True              #creates a lock attribute to lock doors
        self.__key_needed = key_needed  #says what key is needed to unlock this door
    
    def __str__(self):
        """ creates a display message for doors
        --created if statement so string prints out with if the door is locked or unlocked
        """
        if self.get_lock() == True:     #have to use get methods to get the locked status of the door
            locked = 'locked'
        elif self.get_lock() == False:
            locked = 'unlocked'
            
        return "{}\n=====\n{}\n This door is {}.".format(self.__name, self.__description, locked)
        
    def set_lock(self):
        """ method to set the lock attribute to true or false. if the key is with a locked door, the door will unlock """
        
        #try and except for if they don't have the key
        try:
            if self.__key_needed in Player.__invintory: # *******************create Player class with invintory attribute***************
                self.__lock = False
        except:
            print("You do not have the {self.__key} needed to unlock this door.")
            
    def get_lock(self):
        """ method to get the status of the lock to see if the door is unlocked or locked"""
        return self.__lock
    
    def unlock_door(self):
        """ method made to unlock the door"""
        try:
            if self.__lock == True:       #checks to see if the door is locked.
                self.set_lock()           # if door is locked method set_lock is called
        except:                           # if door is not locked message is displayed saying door is already unlocked
            print("The door is already unlocked.")
            
    
        
            
        
        


class Money(Item):
    """class that creates the basics of a monitary object that can be specified in specific game file/classes """
    #subclass of Items class that deals with gold/treasure/money
    def __init__(self,name, description, value, weight, can_pickup, can_drop, amount):
        # called the superclass/baseclass(Items) constructor, it needs to be called if it is not exactly like the superclass's
        super().__init__(name = "Money", description = "Currency", value = amount, weight = 0, can_pickup = True, can_drop = True)
        # add the attributes that are needed and are not in the superclass
        self.__amount = amount         # defines the amount of this gold
        
        # if a subclass doesn't define its own str method/or other method that the superclass has, the superclass method will be used in its place
        # for this class, the value is the same as the amount so theres no reason to print out both attributes
    
    
    def get_money(self):
         pass
        
class Weapon(Consumable):
    """ Weapon class. subclass of Item class
        Specific items can be created for this with json objects/text files/classes in specific my game files """
    
    def __init__(self,name,description,value,weight, can_pickup, can_drop, damage, durability):
        # called the superclass/baseclass(Items) constructor, it needs to be called if it is not exactly like the superclass's
        super().__init__(name, description, value, weight, can_pickup = True, can_drop = True)
        # add the attributes that are needed and are not in the superclass
        self.__damage = damage         # defines the amount of damage the weapon does
        self.__durability = durability # defines the durability of the weapon
        
    def __str__(self):
        """ method that gives readable display of weapons"""
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDurability: {}\n".format(self.name, self.description, self.value, self.get_damage(), self.get_durability())
    
    def set_damage(self, damage):
        """ sets the damage attribute of the weapon"""
        self.__damage = damage
        
    def get_damage(self):
        """ gets the damage amount that the weapon can do"""
        return self.__damage
    
    def set_durability(self, durability):
        """ sets the damage attribute of the weapon"""
        self.__durability = durability
        
    def get_durability(self):
        """ gets the damage amount that the weapon can do"""
        return self.__durability   
    



""" Tests to see if code works"""

        
        