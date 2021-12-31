from player import Player
#from tiles import MapTile

class Action():
    """class that has all the commands/actions that the player can do"""
    
    def __init__(self, method, name, hotkey,**kwargs):
        self.__method = method
        self.__hotkey = hotkey
        self.__name = name
        self.__kwargs =kwargs
        
    def __str__(self):
        return "{}: {}".format(self.__hotkey, self.__name)
    
class MoveNorth(Action): 
    def init(self):  
        #sends to code to player class move_north method to complete action
        super().init(method=Player.move_north, name='Move north', hotkey='n') 

class MoveSouth(Action): 
    def init(self): 
        #sends to code to player class move_north method to complete action
        super().init(method=Player.move_south, name='Move south', hotkey='s')

class MoveEast(Action): 
    def init(self): 
        #sends to code to player class move_north method to complete action
        super().init(method=Player.move_east, name='Move east', hotkey='e')

class MoveWest(Action): 
    def init(self): 
        #sends to code to player class move_north method to complete action
        super().init(method=Player.move_west, name='Move west', hotkey='w')

class ViewInventory(Action):
    """Prints the player's inventory""" 
    def init(self): 
        #sends to code to player class print_invintory method to complete action
        super().init(method=Player.print_inventory, name='View inventory', hotkey='i')
        
# class DropItem(Action):
#     """Player drops something in the room they are in"""
#     def init(self):
#         super().init(method=MapTile.drop_item, name='Drop Item', hotkey='r')
    
# class PickupItem(Action):
#     """Player picks up something and puts it into their invintory"""
#     def init(self):
#         super().init(method=Player.pickup_item, name='Pickup Item', hotkey='g')
        
        

        
