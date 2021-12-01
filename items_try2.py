import json

class Items:
    """ Base class for all items"""
    
    def __init__(self, name, description, value, weight, carryable):
        self.__name = name
        self.__description = description
        self.__value = value
        self.__weight = weight
        self.__carryable = carryable
        
        
    
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

        
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "A pocket knife, good for self-defence."
        self.damage = 5
        self.value = 1


class NailGun(Weapon):
    def __init__(self):
        self.name = "Nail Gun"
        self.description = "An old abandoned nail gun, surprisingly servicable."
        self.damage = 10
        self.value = 15


class Chainsaw(Weapon):
    def __init__(self):
        self.name = "Chainsaw"
        self.description = "A well-maintained chainsaw, might be more effective"\
            "than your current weapon."
        self.damage = 20
        self.value = 25

'''
class (Weapon):
    def __init__(self):
        self.name = ""
        self.description = ""
        self.damage = 30
        self.value = 50
'''
class LasGun(Weapon):
    def __init__(self):
        self.name = "LasGun"
        self.description = "Does a ton of damage, no recoil and lookin' cool doing it."
        self.damage = 70
        self.value = 100

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Bandaid(Consumable):
    def __init__(self):
        self.name = "Bandaid"
        self.healing_value = 10
        self.value = 20


class HealingStim(Consumable):
    def __init__(self):
        self.name = "Healing Stim"
        self.healing_value = 50
        self.value = 60

class NanoHeal(Consumable):
    def __init__(self):
        self.name = "Healing Stim"
        self.healing_value = 100
        self.value = 85


class PuzzlePiece:
    def __init__(self):
        raise NotImplementedError("Do not create raw Puzzle Piece objects.")

    def __str__(self):
        return "{}".format(self.name)


class KeyCard(PuzzlePiece):
    def __init__(self):
        self.name = "Key"
        self.value = 10

class Key(PuzzlePiece):
    def __init__(self):
        self.name = "Key"
        self.value = 10