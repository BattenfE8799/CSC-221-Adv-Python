import items, actions, world

class MapTile:
    """ provides template for all the tiles in the world. Also called an abstract class, as no instances will be created with it, just subclasses"""
    
    def __init__(self, x, y):
        self.__x = x #x is xcoordinate 
        self.__y = y #y is ycooridinate
        self.__box = {} #room container
        
    def intro_text(self):
        raise NotImplementedError() # will warn us if we accidently create a MapTile directly

    
    
    def modify_player(self, player):
        """ actions that take place when the player enteres the tile, and change the state of the player."""
        raise NotImplementedError() #this will cause an error, its just a placeholder for all the other tiles.
        # ^^ will warn us if we accidently create a MapTile directly
    
    
    def adjacent_moves(self):
        """returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y): #moves one tile to left 
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):  #moves one tile to right
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):  #moves one tile to top
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):  #moves one tile to bottom
            moves.append(actions.MoveSouth())
        return moves
    
    def available_actions(self):
        """returns all the avaiable actions in the room"""
        moves = self.adjacent_moves() 
        moves.append(actions.ViewInvintory())
        moves.append(actions.DropItem())
        moves.append(actions.PickupItem())
        return moves
    
    
     
# commented out do to transfering this to the my game file instead.        
# class StartingRoom(MapTile):
#     """   """
#     def intro_text(self):
#         return " ***Enter descirtion*** 
        
    
        