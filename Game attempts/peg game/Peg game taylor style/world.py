# import random
# import enemies
# import Characters
# import items

_world = {}

starting_position = (0, 0)

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
                            The Peg Game!
        
        ** MESSAGE **
        _________________________________________________________
        To win: remove all but one peg!
        _________________________________________________________
        
        To remvoe a peg you must jump into an empty space on the
        other side of the peg next to the one you want to move!
        Good luck!
        """


class PegSpace1(MapTile):
    """Peg space 1"""
    def init(self, x, y):
        super().__init__(self, x, y)
        self.space = True

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
            if tile_name == '':
                _world[(x,y)] = None
            else:
                getattr(('world'), tile_name)(x, y)



# class EnemyTile(MapTile):
#     def __init__(self, x, y):
#         r = random.randint(1,3)
#         if r == 1:
#             self.enemy = enemies.FaceSucker()
#             self.alive_text = "A giant face sucker jumps down from " \
#                               "its broken egg in front of you!"
#             self.dead_text = "The corpse of a dead face sucker lies there motionless on " \
#                              "the ground."
#         elif r == 2:
#             self.enemy = enemies.WorkerAlien()
#             self.alive_text = "A worker alien runs towards you holding a wrench."
#             self.dead_text = "You slayed the worker alien! Good Job!"
#         elif r == 3:
#             self.enemy = enemies.SoldierAlien()
#             self.alive_text = "You spot an Alien holding a rifle in the distance... he spotted you too!"
#             self.dead_text = "That was a valiant effort nice work!"

#         super().__init__(x, y)

    # def intro_text(self):
    #     text = "Peg game"
    #     # text = self.alive_text if self.enemy.is_alive() else self.dead_text
    #     return text

    # def modify_player(self, player):
    #     print("dont need this")
    #     if self.enemy.is_alive():
    #         player.hp = player.hp - self.enemy.damage
    #         print("Enemy does {} damage. You have {} HP remaining."
    #               .format(self.enemy.damage, player.hp))


# class TraderTile(MapTile):
#     def intro_text(self):
#         return """
#         A blinking console is visible in the distance...
#         Its a trading station it might have some good items availible.
#         """

#     def __init__(self,x,y):
#         self.trader = Characters.Trader()
#         self.weapon = Characters.RandomWeapon()
#         self.heals  = Characters.RandomHeals()
#         self.generated_items = False
#         super().__init__(x, y)

#     def trade(self, buyer, seller, randomWeapon, randomHeals):
#         if self.generated_items == False:
#             for _ in range(2):
#                 r = random.randint(0,3)
#                 item = randomWeapon.inventory[r]
#                 seller.inventory.append(item)
#             for _ in range(4):
#                 r = random.randint(0,1)
#                 item = randomHeals.inventory[r]
#                 seller.inventory.append(item)
#                 self.generated_items = True
                
#         for i, item in enumerate(seller.inventory, 1):
#             print("{}. {} - {} Gold".format(i, item.name, item.value))
            
#         while True:
#             user_input = input("Choose an item or press Q to exit: ")
#             if user_input.lower() == "q":
#                 return
#             else:
#                 try:
#                     choice = int(user_input)
#                     to_swap = seller.inventory[choice - 1]
#                     self.swap(seller, buyer, to_swap)
#                 except ValueError:
#                     print("Invalid Choice!")
#                 except IndexError:
#                     print("Invalid Choice!")
                    
    # def swap(self, seller, buyer, item):
    #     if item.value > buyer.spaceCred:
    #         print("That's too expensive")
    #         return
    #     seller.inventory.remove(item)
    #     buyer.inventory.append(item)
    #     seller.spaceCred = seller.spaceCred + item.value
    #     buyer.spaceCred = buyer.spaceCred - item.value
    #     print("Trade Complete!")

    # def check_if_trade(self, player):
    #     while True:
    #         print("Would you like to (B)uy, (S)ell, or (Q)uit?")
    #         user_input = input()
    #         if user_input.lower() == "q":
    #             return
    #         elif user_input.lower() == "b":
    #             print("Here's whats available to buy: ")
    #             self.trade(buyer = player, seller = self.trader, randomWeapon = self.weapon, randomHeals = self.heals)
    #         elif user_input.lower() == "s":
    #             print("Here's whats available to sell: ")
    #             self.trade(buyer=self.trader, seller=player, randomWeapon = self.weapon, randomHeals = self.heals)
    #         else:
    #             print("Invalid choice!")


# class FindCredsTile(MapTile):
#     def __init__(self, x, y):
#         self.spaceCred = random.randint(1, 50)
#         self.creds_claimed = False
#         super().__init__(x, y)

#     def modify_player(self, player):
#         if not self.creds_claimed:
#             self.creds_claimed = True
#             player.spaceCred = player.spaceCred + self.spaceCred
#             print("+{} space credits added.".format(self.spaceCred))

#     def intro_text(self):
#         if self.creds_claimed:
#             return"""
#             You have already gathered the loose space credits in this room 
#             """
#         else:
#             return"""
#             You see a couple of you dead crew mates in the corner.
#             You go over to inspect there bodies.
            
#             You found some space credits near there bodies.
            
#             "There not going to need this anymore." thinking to yourself.
#             """


# class BossRoom(MapTile):
#     def __init__(self, x, y):
#         self.enemy= enemies.MotherAlien()
#         self.alive_text = "A pissed off alien four times the size of a worker alien drops down from the ceiling. \nShe looks pissed that you have killed her babies."
#         self.dead_text = "The corpse of the mother alien lies on the ground you see something shinny in her mouth.\n\nIt's a Key!\n\
#                           You place the key in the door and it opens the way to the escape pods"

#         super().__init__(x, y)
        
#     def intro_text(self):
#         text = self.alive_text if self.enemy.is_alive() else self.dead_text
#         return text

#     def modify_player(self, player):
#         if self.enemy.is_alive():
#             player.hp = player.hp - self.enemy.damage
#             print("Enemy does {} damage. You have {} HP remaining."
#                   .format(self.enemy.damage, player.hp))
#         if not self.enemy.is_alive():
#             player.inventory.append(items.Key())
        

# """
#     dsl = (D)oc (S)tring (L)iteral
# """


# def is_dsl_valid(dsl):
#     if dsl.count("|ST|") != 1:
#         return False
#     if dsl.count("|ET|") == 0:
#         return False
#     lines = dsl.splitlines()
#     lines = [l for l in lines if l]
#     pipe_counts = [line.count("|") for line in lines]
#     for count in pipe_counts:
#         if count != pipe_counts[0]:
#             return False

#     return True


# def parse_world_dsl():
#     if not is_dsl_valid(world_dsl):
#         raise SyntaxError("Doc String Literal is invalid")

#     dsl_lines = world_dsl.splitlines()
#     dsl_lines = [x for x in dsl_lines if x]

#     for y, dsl_row in enumerate(dsl_lines):
#         row = []
#         dsl_cells = dsl_row.split("|")
#         dsl_cells = [c for c in dsl_cells if c]
#         for x, dsl_cell in enumerate(dsl_cells):
#             # tile_type = tile_type_dict[dsl_cell]
#             if tile_type == StartTile:
#                 global start_tile_location
#                 start_tile_location = x, y
#             row.append(tile_type(x, y) if tile_type else None)

#         world_map.append(row)


# def tile_at(x, y):
#     if x < 0 or y < 0:
#         return None
#     try:
#         return world_map[y][x]
#     except IndexError:
#         return None


# world_dsl = """
# nothing here to see
# """

# world_map = []

# tile_type_dict = {"ET": EscapeTile,
#                   "EN": EnemyTile,
#                   "ST": StartTile,
#                   "FC": FindCredsTile,
#                   "TT": TraderTile,
#                   "BR": BossRoom,
#                   "BT": BoringTile,
#                   "  ": None}
