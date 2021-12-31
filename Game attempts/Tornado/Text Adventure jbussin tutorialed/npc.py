""" class that creates enemies """


class NPC:
    """ class that creates npcs, helps create enemies class"""
    
    def __init__(self, name, description, hp):
        self.__name = name                 #creates name of npc
        self.__description = description   #creates description of npc
        self.__health_points = hp           #creates health points for npc
        
        
    def __str__(self):
        return "{}\n=====\n{}\n".format(self.__name, self.__description)


    def is_alive(self):
        """sets whether or not npc is alive"""
        if self.__health_points <= 0:
            return False
        else:
            return True
    

    def set_hp(self, hp):
        """ method to adjust hp: from potions or damage etc"""
        if hp < self.__health_points:
            self.__health_points = hp
            
    def get_hp(self):
        """ method used to get hp"""
        return self.__health_points
    
class Enemy(NPC):
    """ class that creates enemies"""
    
    def __init__(self, name, description, hp, damage, drops):
        super().__init__(name, description, hp)  #creates connection for enemy name and description
        self.__enemy_drops = drops       #creates attribute that is a list of items the enemy can drop

    def __str__(self):
        """ class that displays information on the enemey, their name, health points, and description"""
        return "{} HP: {}\n=====\n{}\n".format(self.__name, self.__health_points, self.__description)    
    
    
    """ maybe create instances for enemies"""
    
class Traders(NPC):
    """ class that creates traders """
    def __init__(self, name, description, amount, invintory):
        super().__init__(name, description) #calls NPC constructor for attributes
        self.__money_amount = amount        #creates how much money the shop/trader has
        self.__npc_invintory = invintory    #creates invintory for shop
        
    #doesn't need __str__ method, because it only needs name and description
    
        
    
    
    
        
    
        

        
    

