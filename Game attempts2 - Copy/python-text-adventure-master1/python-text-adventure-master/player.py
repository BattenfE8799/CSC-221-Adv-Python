import random
import tiles

__author__ = 'Phillip Johnson'


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
        self.location_x, self.location_y = tiles.starting_position
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
        print(tiles.tile_exists(self.location_x, self.location_y).intro_text())

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

