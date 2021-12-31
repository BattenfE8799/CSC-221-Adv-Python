# -*- coding: utf-8 -*-
"""
Game engine
v1- 
 --setting up dataclasses for baseitems and containers and rooms
 
"""
from dataclasses import dataclass #enables use of dataclass
import json                       #import json to use json objects and files

@dataclass
class BaseItem:
    name: str
    description: str
    
    def __str__(self):
        return f'{self.name}: {self.description}'

@dataclass
class Container(BaseItem):
    contents: list
    
    def __str__(self):
        return f'{self.name}: {self.description}, Contains: {self.contents}'
    
    def list_contents(self):
        """prints items from the dictionary"""
        text = ''
        if self.contents == []:
            print("Nothing here.")
        else:
            for item in self.contents:
                print(item)
                text += str(item) +"\n"
                return text
    def addItem(self, item):
        """ used to add an item into a room. """
        self.contents.append(item)
    
    def removeItem(self, item):
        """ used to remove items from a room. """
        if item in self.contents:
            self.remove(item)
@dataclass
class Player(Container):
    location = str = None
    win = bool = False
    partial_win = bool = False
    is_alive = bool = True    
            

@dataclass
class Room(Container):
    exits: dict
    door: str = None
    lockedexit: str = None
    
    def look(self):
      """ contains the name, description, and exits in a human-readable fashion"""
      text = f'\n{self.name}:\n{self.description}\n\nExits from room:\n'
      #adds exits
      # text = ''
      exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
      for direction in exitList:
          text += direction                     # North, South, etc. 
          text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
          text += "\n"
      # adds items in room if there are any
      text += "\nIn this room are: \n"
      # f'{fName:<10s}{" ":4}{lName:<10s}
      if len(self.contents) == 0:
          text += "\nNothing you need in here."
      else:
          listcontents = self.list_contents()
          text += listcontents
      if self.door != None:
          text += "\n\nThere is a door here to the: " + self.lockedexit + "\n"
          text += self.door.name + " "
          text += self.door.description
      return text
  
    
    def addDoor(self, door, lockedexit):
        self.door = door
        self.lockedexit = lockedexit

@dataclass
class Door(BaseItem):
    name = str
    description = str
    state = int = 0
    locked = bool = False

    def look(self):
        print("\nDescription: " + str(self.description))
        print("\nLocked: " + str(self.locked))
    def open(self):
        self.state = 1
        self.description = "The door is open."
    def close(self):
        self.state = 0
        self.description = "The door is closed."
    def lock(self):
        self.locked = True
        print("The door is locked.")
    def unlock(self):
        self.locked = False
        print("The door is unlocked.")
    def exits(self):
        if self.locked == False:
            if self.state == 1:
                #door is passable
                return True
            else:
                print("Door is closed.")
                return False
        else:
            return False
    
class Game:
    """ sets up game engine"""
    
    def __init__(self):
        """ Initialize object (with no rooms) """
        self.rooms = {} # stored in dictionary
        self.items = []
        # Player is currently used to hold current location (loc)
        self.player = Player("Player","You are the player.") 
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
        self.end_game = False
    
    
    def commands():
        """commands player can choose"""
        pass
    
    def loop():
        """game loop"""
        pass
    
    def end():
        """ends the game"""
        pass
    
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
        elif verb == 'unlock':
            door = words[1]
            self.commandUnlock(door)
        elif verb == 'open':
            door = words[1]
            self.commandOpen(door)
        elif verb == 'lock':
            door = words[1]
            self.commandLock(door)
        elif verb == 'close':
            door = words[1]
            self.commandClose(door)
        elif verb == 'i':
            self.commandInv()
        else: # first word is verb
            print("I don't know how to", words[0])
            
    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
        if self.here.exits.get(direction) == None:
            print("\nYou can't go that way.")
        if self.here.door != None: 
            if self.here.lockedexit == direction:
                
                if self.here.door.locked == True:
                    print("\nThe door is locked.") 
                    return
                
                if self.here.door.state == 0:
                    print("\nThe door is closed.\n")
                
                    return
            # if door is open and unlocked, go through!

        if self.here.exits.get(direction) != None: # this key does exist
            newRoomName = self.here.exits[direction]
            newRoom = self.rooms[newRoomName]
            self.here = newRoom
            self.here.describe()
    def commandGet(self, itemName):
        """ remove the item from the room (if it's there)
        and place it in player inventory.
        """

        item = None
        for thing in self.here.contents:
            if thing.name == itemName:
                item = thing
        if item != None:    
            self.here.contents.remove(item)
            self.player.contents.append(item)
            # print(self.player.contents)
            print(f'You pickup the {itemName}.')
        else:
            print(f'You cant see any {itemName} here.')        
        
        
    def commandDrop(self, itemName):
        """ 
            remove the item from player inventory
            (if it's there) and add it to the room. 
        """
        
        item = None
        for thing in self.player.contents:
            if thing.name == itemName:
                item = thing
                
        if item != None:    
            self.here.contents.append(item), self.player.contents.remove(item)
            print (f'You drop the {itemName}.')
            
        else:
            print(f'You dont have a {itemName} to drop!')  


    def commandInv(self):
        # self.player.Inventory()
        for item in self.player.contents:
            print(item) 
    
    def commandOpen(self, door):
        door = self.here.door
        # if door.locked != True: 
        if door != None:
            door.open()
            door.look()
                
                
    def commandUnlock(self, door):
        #trying again, with item a callable object
        for thing in self.player.contents:
            if thing == self.items:
                self.here.door.locked = False
                print("The door is unlocked.")
        
    def commandClose(self, door):
        door = self.here.door
        if door != None:
            door.close()
            door.look()
    def commandLock(self, door):
        door = self.here.door
        for thing in self.player.contents:
            if thing == ['key']:
                item = thing
            if item in self.player.contents:
                if door != None:
                    door.lock()
                    door.look()
                    
    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player.location
    
    @here.setter
    def here(self, room):
        self.player.location = room
    
class ItemEncoder(json.JSONEncoder):
    """ encodes items into json file"""
    def default(self, i):
        if isinstance(i, BaseItem):
            return {'name': i.name, 'description': i.description,}
        return super().default()

def Load():
    save_file = 'save.json'
    GameTitle = ""
    Intro = ""
    Ending = ""
    rooms = {}
    items = []
    rooms = {}
    player = Player
    doors = []
    

    
    with open (save_file, 'r') as sf:
        save = json.loads(sf)
        print(save)


def Save(rooms, items, player, filename="save.json"):
    print(rooms, items, player)
    with open (filename, 'w') as f:
        data = json.load(filename)
        temp = data["rooms"]
        y = rooms
        temp.append(y)
        json(data, f, indent = 4)
    
def main():
    print("Starting game -- enter your command.")
    game = Game()
    game.setup()
    game.loop()
    game.end()
        
if __name__ == '__main__':
    # testContainer = Container("Box", "Its a box for testing", ["test sword", "test shield"])
    # testBaseItem = BaseItem("Test key", "Its a key")
    # # testContainer.contents.append(testBaseItem)
    # print("Test Container: ", testContainer)
    # # print("Test item: ", testBaseItem)
    # testContainer.addItem(testBaseItem)
    # print("Test Container: ", testContainer)
    main()
    
    