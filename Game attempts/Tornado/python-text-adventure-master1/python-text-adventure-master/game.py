"""
A simple text adventure designed as a learning experience for new programmers.
"""

import play




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
        pass

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if play.tile_exists(self.x + 1, self.y):
            moves.append(Action.MoveEast())
        if play.tile_exists(self.x - 1, self.y):
            moves.append(Action.MoveWest())
        if play.tile_exists(self.x, self.y - 1):
            moves.append(Action.MoveNorth())
        if play.tile_exists(self.x, self.y + 1):
            moves.append(Action.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(Action.ViewInventory())
        moves.append(Action.Pickup())
        moves.append(Action.Drop())

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

class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Player():
    def __init__(self):
        self.inventory = []
        self.hp = 100
        self.location_x, self.location_y = play.starting_position
        self.win = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(play.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)
        
    # def pickup_item(self, item):
    #     """player picks up item and puts it into their invintory"""
    #     try:
    #         if item.__can_pickup == True:
    #             if item in tiles.tile_exists(self.__location_x, self.__location_y).__box:
    #                 tiles.tile_exists(self.__location_x, self.__location_y).__box.remove(item)
    #                 self.__invintory.append(item)
    #     except:
    #         print("You cannot pick that up.")

    # def attack(self, enemy):
    #     best_weapon = None
    #     max_dmg = 0
    #     for i in self.inventory:
    #         if isinstance(i, items.Weapon):
    #             if i.damage > max_dmg:
    #                 max_dmg = i.damage
    #                 best_weapon = i

    #     print("You use {} against {}!".format(best_weapon.name, enemy.name))
    #     enemy.hp -= best_weapon.damage
    #     if not enemy.is_alive():
    #         print("You killed {}!".format(enemy.name))
    #     else:
    #         print("{} HP is {}.".format(enemy.name, enemy.hp))

    # def flee(self, tile):
    #     """Moves the player randomly to an adjacent tile"""
    #     available_moves = tile.adjacent_moves()
    #     r = random.randint(0, len(available_moves) - 1)
    #     self.do_action(available_moves[r])


class Action():
    """The base class for all actions"""
    def __init__(self, method, name, hotkey, **kwargs):
        """Creates a new action

        :param method: the function object to execute
        :param name: the name of the action
        :param ends_turn: True if the player is expected to move after this action else False
        :param hotkey: The keyboard key the player should use to initiate this action
        """
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')


class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')


# class Attack(Action):
#     def __init__(self, enemy):
#         super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)


# class Flee(Action):
#     def __init__(self, tile):
#         super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

class Pickup(Action):
    def __init__(self):
        super().__init__(method=Player.pickup_item, name="Pickup", hotkey='g')

class Drop(Action):
    def __init__(self):
        super().__init__(method=Container.drop_item, name='Pickup Item', hotkey='g')
        
        
        
