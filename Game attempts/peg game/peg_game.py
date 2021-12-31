""" My game class. Code that has specifics for my game specifically """
# !Includes Specific weapons and items
from items import Weapon, Item, Money
from npc import NPC, Enemy
from tiles import MapTile

""" Does not need player or enemys"""
#actions for player to do



#create world tiles for this game
class StartingRoom(MapTile):
    """   """
    def intro_text(self): #introduction text for the game
        return """The Peg Game: To move a peg, you jump it over one next to it into an empty space.\nIf there is not an empty space on the other side of the peg being jumped, you cannot go that way.\n Once you move your peg, the jumped peg will be removed from the game.\n To win: Leave only 1 peg on the board.\n\n Good Luck!\n"""
    
    def modify_player(self, player):
        #Room has no action on player
        pass #use pass after, to let python know we want to skip that for now

class EmptySpace(MapTile):
    """Space inbetween peg holes"""
    def intro_text(self):
        raise NotImplementedError("Empty Space between peg spaces") #enter the text you want the player to see when they enter the room.

#creates each space that can occupy a peg
class PegSpace1(MapTile):
    """Peg space 1"""
    def init(self, x, y):
        super().__init__(self, x, y)
        self.space = True

    
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
    
    # def remove_peg(self, peg):
    #     try:
    #         if PegSpace4.__space == True or PegSpace4.__space == True: #****TODO***how to jump over a peg into an empty space
            
    #             try: 
    #                 if self.__space == False:
    #                     self.__space == True
    #             except:
    #                 print("There is already a peg there. Try to jump to one with an empty space.")
                    
    #     except:
    #         print("You cannot move there. It is not a jump away.")
                
                
    #     """ if space = true cannot put peg, if space between them has no peg cannot move peg"""
        
                
        
class PegSpace2(MapTile):
    """Peg space 2"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.

class PegSpace3(MapTile):
    """Peg space 3"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace4(MapTile):
    """Peg space 4"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace5(MapTile):
    """Peg space 5"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.        
  
class PegSpace6(MapTile):
    """Peg space 6"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace7(MapTile):
    """Peg space 7"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.

class PegSpace8(MapTile):
    """Peg space 8"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace9(MapTile):
    """Peg space 9"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace10(MapTile):
    """Peg space 10"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
    
class PegSpace11(MapTile):
    """Peg space 11"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace12(MapTile):
    """Peg space 12"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.

class PegSpace13(MapTile):
    """Peg space 13"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace14(MapTile):
    """Peg space 14"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show.
        
class PegSpace15(MapTile):
    """Peg space 15"""
    def intro_text(self):
        pass #passed cause I dont need it for peg game, and don't want implamented error to show. 