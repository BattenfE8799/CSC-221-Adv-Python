import json

class Items:
    """ Base class for all items"""
    
    def __init__(self, name, description, value, weight, carryable):
        self.__name = name
        self.__description = description
        self.__value = value
        self.__weight = weight
        
        #flag commands for inheritance
        self._canGet = True #default to gettable/pickup
        self._canDrop = True #the drop id to see if items can be dropped
        
        
    
    def __str__(self):
        return self.name

    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_description(self, description):
        self.__description = description
        
    def get_description(self):
        return self.__description
    
    def set_value(self, value):
        self.__value = value
        
    def get_value(self):
        return self.__value
    
    def set_weight(self, weight):
        self.__weight = weight
        
    def get_weight(self):
        return self.__weight
        
    def set_carryable(self, carryable):
        self.__carryable = carryable
        
    def get_carryable(self):
        return self.__carryable    
        
class UsableItems(Items):
    """ usableitems class that is specific for usable items, subclass of items"""
    def __init__(self, name, description, value, weight, carryable, durability):
        super().__init__(name, description, value, weight, carryable)
        self._durability = durability

class Weapons(UsableItems):
    """ Weapons class that is specific for weapons items, subclass of  usableitems"""
    def __init__(self, name, description, value, weight, carryable, durability, damage):
        super().__init__(name, description, value, weight, carryable, durability)
        self._damage = damage

class Doors(Items):
    """ doors class that is for doors and locked doors"""
    def __init__(self, name, description, value, weight, carryable, locked):
        super().__init__(name, description, value, weight, carryable)
        self._locked = locked
        
    def set_locked(self, locked):
        self._locked = locked
    
    def get_locked(self):
        return self._locked
    
    def unlock(self, locked, key):
        if locked == 0:
            return True
        elif locked != 0:
            if key == True:
                self.set_locked(0)
                return True
        else:
            print("You have no key for that door. The door remains locked.")
        
