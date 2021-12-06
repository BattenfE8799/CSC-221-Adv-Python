# CSC 221
# Text Adventure
# norrisa
# 10/1/21

import Player


"""
Version history:
    v1 - built using Room references (basically a graph). 
        downside: you have to create all rooms, then link
        them together afterwards.
        
    v2 - used constant room IDs to make it possible to add
        and link rooms in one pass. 
        downside: "this looks like BASIC" (from the peanut gallery)
        
    v3 - realization: if the Room names are unique, that's a
        unique ID. I therefore changed
        the container for all Rooms to be a dictionary --
        now it's easy enough to look up the room by name.


"""

class Game:
    """
    The Game class organizes all game data in a central location.
    Usage:
    - Set up game using your choice of room configurations
      (TODO: Read these from a file in future)
    - call loop()
    """

    def __init__(self):
        """ Initialize object (with no rooms) """
        self.rooms = { } # stored in dictionary
        # Player is currently used to hold current location (loc)
        self.player = Player.Player("Player","You are the player.") 
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
        

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def output(self, message):
        """ output the message. Just uses print() in base class.
        You might for example subclass to use Flask, etc. """
        print(message)

    
    # def setup(self):
    #     """ setup(): create a graph of rooms for play. """
    #     # loader = MyGameLoader()
    #     # self.rooms = loader.setup()
        
    #     # starting location
    #     self.here = self.rooms["Bedroom"]
    #     # Let's do a turn 1 look , to orient the player
    #     self.here.describe()
        
        

    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing")
        


    def end(self):
        """Ends the game, explaining the  turns played"""
        self.won()
        if self.player.partial_win == False:
            print("You didn't win, the torndao took your family.\n It took you {turns_counted} turns to end the game!")
        elif self.player.win == False:
            print("You didn't get everyone to safety! You lose!\n It took you {turns_counted} turns to end the game!")
        elif self.player.partial_win == True:
            print("You won...technically...what about the pets?\n It took you {turns_counted} turns to end the game!")
        elif self.player.win == True:
            print(f'You Won! Eveyone you love is safe from the tornado! Including your pets!\n It took you {self.turns_counted} turns to end the game!')
        
    
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input(">")
        command = command.lower()
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            self.commandGo(direction)    
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")
        elif verb == "get":
            item = words[1]
            self.commandGet(item)
        elif verb == "drop":
            item = words[1]
            self.commandDrop(item)
        
        else: # first word is verb
            print("I don't know how to", words[0])

    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            newRoomName = self.here.exits[direction]
            newRoom     = self.rooms[newRoomName]
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()
    
    def commandGet(self, itemName):
        """ remove the item from the room (if it's there)
        and place it in player inventory.
        """
        # TODO: actually do this
        # We'll need to remove the item from the current
        # room, and then add it to the player inventory
        # (which means we need a player inventory)
        print("You try to get the", itemName)
        # self.here.list_contents()
        # print(itemName)
        # self.get_item(itemName)
        if itemName in self.here.contents:
            self.contents.remove(itemName)
            self.player.contents.append(itemName)
            print("You pick up the ",itemName,".")
        else:
            print("You can't see any", itemName, "here.")        
        
    # def give_item(self, item):
    #     """gives the npc an item"""
    #     if item in self.player.contents:
    #         self.contents.append(item)
    #         self.player.contents.remove(item)
    #         print("You pick up the ",item,".")
    #     else:
    #         print("You can't see any", item, "here.")
            
    def get_items(self, item):
        if item in self.here.contents:
            self.contents.remove(item)
            self.player.contents.append(item)
        
        # if self.here.contains(itemName):
        #     item = self.here.contents[itemName]
        #     self.here.moveItemTo(item, self.player)
        #     print("You pick up the ",itemName,".")
        # else:
        #     print("You can't see any", itemName, "here.")
        
            
            

        
        
    def commandDrop(self, itemName):
        """ remove the item from player inventory
        (if it's there) and add it to the room. 
        """
        print("You try to drop the", itemName)
        
        if self.player.contains(itemName):
            item = self.player.contents[itemName]
            self.player.moveItemTo(item, self.here)
            print("You drop the", itemName,".")
        else:
            print("You don't have a", itemName, "to drop!")

    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player.loc
    
    @here.setter
    def here(self, room):
        self.player.loc = room

def main():
    print("Starting game -- enter your command.")
    game = Game()
    game.setup()
    game.loop()
    game.end()


if __name__ == "__main__":
    main()
