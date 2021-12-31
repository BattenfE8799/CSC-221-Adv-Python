"""Describes the tiles in the world space."""
__author__ = 'Phillip Johnson'

import items, enemies, actions, world


class MapTile:
    """The base class for a tile within the world space"""
    def __init__(self, x, y):
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


# class StartingRoom(MapTile):
#     def intro_text(self):
#         return """
#          You're in your bathroom when you get a Tornado warning on your phone.\n
#         A tornado is heading your way!\n You need to get to the tornado shelter in the back yard!
#         """

#     def modify_player(self, the_player):
#         #Room has no action on player
#         pass


# class EmptyCavePath(MapTile):
#     def intro_text(self):
#         return """
#         Another unremarkable part of the cave. You must forge onwards.
#         """

#     def modify_player(self, the_player):
#         #Room has no action on player
#         pass

class StartingRoom(MapTile):
    """   """
    def intro_text(self): #introduction text for the game
        return """You wake up in your bed.\nLooking at the clock you see its already noon.\n Your phone dings with a weather alert notification.\n Panic grips you as you realize a tornado is heading right toward your house!\n"""
    
    def modify_player(self, player):
        #Room has no action on player
        pass #use pass after, to let python know we want to skip that for now

class BedR(MapTile):
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
class Stairs(MapTile):
    """The stairs that go to the second floor and attic"""
    def intro_text(self):
        return """ TODO"""

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
    
    
    


# class LootRoom(MapTile):
#     """A room that adds something to the player's inventory"""
#     def __init__(self, x, y, item):
#         self.item = item
#         super().__init__(x, y)

#     def add_loot(self, the_player):
#         the_player.inventory.append(self.item)

#     def modify_player(self, the_player):
#         self.add_loot(the_player)


# class FindDaggerRoom(LootRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, items.Dagger())

#     def intro_text(self):
#         return """
#         You notice something shiny in the corner.
#         It's a dagger! You pick it up.
        


# class Find5GoldRoom(LootRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, items.Gold(5))

#     def intro_text(self):
#         return """
#         Someone dropped a 5 gold piece. You pick it up.
#         """


# class EnemyRoom(MapTile):
#     def __init__(self, x, y, enemy):
#         self.enemy = enemy
#         super().__init__(x, y)

#     def modify_player(self, the_player):
#         if self.enemy.is_alive():
#             the_player.hp = the_player.hp - self.enemy.damage
#             print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

#     def available_actions(self):
#         if self.enemy.is_alive():
#             return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
#         else:
#             return self.adjacent_moves()


# class GiantSpiderRoom(EnemyRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, enemies.GiantSpider())

#     def intro_text(self):
#         if self.enemy.is_alive():
#             return """
#             A giant spider jumps down from its web in front of you!
#             """
#         else:
#             return """
#             The corpse of a dead spider rots on the ground.
#             """


# class OgreRoom(EnemyRoom):
#     def __init__(self, x, y):
#         super().__init__(x, y, enemies.Ogre())

#     def intro_text(self):
#         if self.enemy.is_alive():
#             return """
#             An ogre is blocking your path!
#             """
#         else:
#             return """
#             A dead ogre reminds you of your triumph.
#             """


# class SnakePitRoom(MapTile):
#     def intro_text(self):
#         return """
#         You have fallen into a pit of deadly snakes!

#         You have died!
#         """

#     def modify_player(self, player):
#         player.hp = 0


# class LeaveCaveRoom(MapTile):
#     def intro_text(self):
#         return """
#         You see a bright light in the distance...
#         ... it grows as you get closer! It's sunlight!


#         Victory is yours!
#         """

#     def modify_player(self, player):
#         player.victory = True


