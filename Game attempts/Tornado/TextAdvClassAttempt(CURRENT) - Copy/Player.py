# Player class
from Container import Container
class Player(Container):
    """
    Any data relating to the player himself should go in the 
    Player class.
    """
    
    def __init__(self, name, description):
        super().__init__(name, description)
        self.loc = None # what room is the player in?
        self.contents = [] # because we're also a container
        self.win = False
        self.partial_win = False
        self.is_alive = True
        
    def __str__(self):
        pass
        #itemlist = []
        # for item in self.contents:
        #     itemlist.append(item)
        # if itemlist == []:
        #     return f"It's you...\n You have nothing with you.\n You're in your {self.loc}"
        # else:    
        #     return f"It's you...\n You have: {itemlist}.\n You're in your {self.loc}"
        


# def testing():
#     """tests player class"""
#     print("\nStarting: player Class test\n@@@@@@@@@@@@@@@")
#     player = Player('Player', 'You.')
#     print("created player now get your location:")
#     print(player.loc)
#     print("description at self/player: ")
#     print(player)
#     print("trying to move the player wheres theres no exit:")
#     verb = input()
#     direction = input()
#     Game.Game.commandGo(verb, direction)
#     print(player)
#     print("trying to move the player:")
#     direction = input()
#     Game.Game.commandGo(direction)
    
#     print("\nEnd of: player class test\n@@@@@@@@@@@@@@@")

# if __name__ == "__main__":
#     testing()
