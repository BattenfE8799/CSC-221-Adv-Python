""" My game class. Code that has specifics for my game specifically """
# !Includes Specific weapons and items
from npc import NPC
from tiles import MapTile

"""load correct resource file for world"""


#class Key(Item):
  #  pass #use pass after a class to let python know we want to skip that for now
    
#Specific Items for my game
#keys and puzzle items, and doors

#specific npcs for my game
#create family and/or friends to save from the tornado

class Family(NPC):
    """ class that specifies for my game npcs"""
    
    def __init__(self, name, description, hp):
        super().__init__(self, name, description, hp)
        self.__requirement_met = False     #creates name of npc
        self.__description   #creates description of npc
        self.__health_points = hp           #creates health points for npc
        #self.__requirements = requirements
        
    def familyObjects(self):
        """creates family objects. instead of classes"""
        Nana = self("Nana","Your mother, an old woman who is not in the best health. She's not getting along with Papaw.",1)
        Papaw = self("Papaw","Your father, who recently had laser eye surgery and cannot see. He's not getting along with Nana.",10)
        Spouse = self("Spouse","Your loving spouse. Cares more about the kids than theirself.", 50)
        Child = self("Child", "Your youngest, a sleepy toddler. Will not walk" , 50)
        Teen = self("Teen", "Your oldest, a cranky teen who has their broken hand in a cast. Their other they got stuck in a jar...", 70)
        Dog = self("Dog", "Your family's dog. It's petrified because of the weather.", 80)
        Cat = self("Cat", "Your family's cat. It's just a fluffy overlord.", 100)
        Snake = self("Snake", "Its your pet ball python.", 100)
        Bird = self("Bird","Its your spouce's pet bird.", 100)
        






class StartingRoom(MapTile):
    """   """
    def intro_text(self): #introduction text for the game
        return """You wake up in your bed.\nLooking at the clock you see its already noon.\n Your phone dings with a weather alert notification.\n Panic grips you as you realize a tornado is heading right toward your house!\n"""
    
    def modify_player(self, player):
        #Room has no action on player
        pass #use pass after, to let python know we want to skip that for now

class BathR(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class NanaR(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class ChildR(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Attic(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class LivingR(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class DiningR(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class Kitchen(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Hall(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class PapawR(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Fyard(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Syard(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Byard(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class Shed(MapTile):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class Shelter(MapTile):
    def intro_text(self):
        return """TODO"""
# class Shelter(MapTile):
#     """the shelter"""
#     def __init__(self, x, y):
#         super().__init__(self, x, y)
#         self.__win_conditions = [Family.familyObjects.Nana, Family.familyObjects.Papaw, Family.familyObjects.Spouce, Family.familyObjects.Child, Family.familyObjects.Teen]
#         self.__actual_win_conditions = [Family.familyObjects.Nana, Family.familyObjects.Papaw, Family.familyObjects.Souce, Family.familyObjects.Child, Family.familyObjects.Teen, Family.familyObjects.Dog, Family.familyObjects.Cat, Family.familyObjects.Snake, Family.familyObjects.Bird]
#         self.__shelter_box = [] #list of the things and people in shelter
#     def intro_text(self):
#         """intro text when they go into the room, plus checking to see if they won."""
#         matches1 = all(elem in self.__shelter_box for elem in self.__actual_win_conditions)
#         matches2 = all(elem in self.__shelter_box for elem in self.__win_conditions)
#         if matches1:
#             return """Everyone you care about is in the shelter, including your pets! Just in time, as the tornado blowes down your house."""
#         if matches2:
#             return """Are you sure you are done? All of your family are here, as is the dog, but it feels as if something is missing..."""
    
    
    
