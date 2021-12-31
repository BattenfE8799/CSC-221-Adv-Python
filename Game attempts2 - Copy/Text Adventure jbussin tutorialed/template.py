"""
Template for your specific adventure game
"""
# !Includes Specific weapons and items

from items import Weapon, Item, Money
from npc import NPC, Enemy
from tiles import MapTile

#create monitary coin

#create npcs and 

class Enemy(NPC):
    """ class that creates enemies"""
    
    def __init__(self, name, description, hp, damage, drops):
        super().__init__(name, description, hp)  #creates connection for enemy name and description
        self.__enemy_drops = drops 
spider_drops[Item.money()]
giant_spider = Enemy("Giant Spider", "Its a giant spider.", 10, )
# class GiantSpider(Enemy):
#     def __init__(self): 
#         super().init(name="Giant Spider", hp=10, damage=2)

# class Ogre(Enemy): 
#     def init(self): 
#         super().init(name="Ogre", hp=30, damage=15)

#create items, and doors


#create map tiles in the game

class StartingRoom(MapTile):
    """The starting room"""
    def intro_text(self): 
        return """TODO"""  #this is where you put the introduction text for the game\
        
    def modify_player(self, player):
        #this is made because if it doesn't override the superclass, the superclass will execute, and raise the error
        #Room has no action on player
        pass #use pass after, to let python know we want to skip that for now
    
class LootRoom(MapTile):
    """ a class for tiles where a player will find a new item"""
    def __init__(self, x, y, item):
        super().__init__(x,y) #location as found in superclass
        self.__item = item #the item found in the room
        
    def add_loot(self, player):
        """ adds the item to the player's invintory"""
        player.invintory.append(self.__item)
        
    def modify_player(self, player):
        """ sends to add_loot, to add item found into the player's invintory"""
        self.add_loot(player)
        
class EnemyRoom(MapTile):
    """Tile with an enemy in it"""
    def __init__(self, x, y, enemy):
        super().__init__(x,y) #gets location from superclass
        self.__enemy = enemy #says what enemy is in room
    
    def modify_player(self, the_player):
        """player's hp takes damage from enemy if enemy is alive"""
        if self.__enemy.is_alive(): #checks to see if enemy is alive
            the_player.hp = the_player.hp - self.__enemy.damage #if enemy is alive player takes damage to their hp
            print("{} does {} damage. You have {} HP remaining.".format(self.__enemy, self.__enemy.damage, the_player.hp))

class EmptyRoom(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    


            
    
    
    