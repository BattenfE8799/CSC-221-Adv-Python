"""Describes the tiles in the world space."""
__author__ = 'Phillip Johnson'

from actions import Action
import tiles
_world = {}
starting_position = (0, 0)

def tile_exists(x, y):
        """Returns the tile at the given coordinates or None if there is no tile.

        :param x: the x-coordinate in the worldspace
        :param y: the y-coordinate in the worldspace
        :return: the tile at the given coordinates or None if there is no tile
        """
        return _world.get((x, y))


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

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
        if tiles.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if tiles.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if tiles.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if tiles.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Pickup())
        moves.append(actions.Drop())

        return moves

class Container(MapTile):
    def __ini__(self, x, y):
        super().__init__(self, x, y)
        self.__box = []
        

class StartingRoom(Container):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, the_player):
        #Room has no action on player
        pass

class BedR(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class NanaR(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class ChildR(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Attic(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class LivingR(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class DiningR(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class Kitchen(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Hall(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class PapawR(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Fyard(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Syard(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.
    
class Byard(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class Shed(Container):
    """template to create your own specific tile"""
    def intro_text(self):
        return """TODO""" #enter the text you want the player to see when they enter the room.

class Stairs(Container):
    def intro_text(self):
        return "ToDO"
    
class Shelter(Container):
    def intro_text(self):
        return """TODO"""
# class EmptyCavePath(MapTile):
#     def intro_text(self):
#         return """
#         Another unremarkable part of the cave. You must forge onwards.
#         """

#     def modify_player(self, the_player):
#         #Room has no action on player
#         pass


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
#         """


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
