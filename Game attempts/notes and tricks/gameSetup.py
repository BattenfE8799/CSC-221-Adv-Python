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
    
    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = f'\n{self.name}:\n{self.description}\n\n'
        text += 'Exits: \n'
        exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
        return text
  
    def describe(self):
        """ print full room description. """
        print(self)
    
    def look(self):
        """looks at items in room"""
        print(self)
        
        text = "\nIn this room are: \n"
        if self.contents == []:
             text += "\nNothing you need in here."
        else:
            print(text)
            for item in self.contents:
                print(item)
            
        if self.door != None:
            text = "\nThere is a door here to the: " + self.lockedexit + "\n"
            text += self.door.name + " "
            text += self.door.description
        print(text)
    
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
        self.title = "Game Title"
        self.intro = "Game Intro"
        self.ending = "Game Ending"
        self.roomslist = {} # stored in dictionary
        self.items = []
        self.doors = []
        # Player is currently used to hold current location (loc)
        self.player = Player("Player","You are the player.", 'contents'== []) 
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
        self.end_game = False
    
    
    def loop(self):
        """game loop"""
        turn_counter = 0
        player = self.player
        print(self.title)
        print(self.intro)
        
        while player.is_alive == True:
            win = player.win()
            if win == True:
                break
            turn_counter += 1
            self.playerAction()
        self.end()
        pass
            
            
    
    def end(self):
        """ends the game"""
        print(self.ending)
        exit
    
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
            self.here.look()
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
        elif verb == 'inv':
            self.commandInv()
        elif verb == 'save':
            self.Save()
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
        
    def Load(self):
        with open ('save.json', 'r') as save_file:
            data = json.load(save_file)
            self.title = data["Title"]
            self.intro = data["Intro"]
            self.ending = data["Ending"]
            # self.rooms = data["rooms"]
            # self.items = data["items"]
            # self.doors = data["doors"]
            # self.player = data["player"]
            print("Game Loaded")
            
            
    
    
    def Save(self, filename="save.json"):
        with open (filename, 'w') as f:
            data = json.load(filename)
            temp = data["rooms"]
            y = self
            temp.append(y)
            json(data, f, indent = 4)

    
    
    
class ItemEncoder(json.JSONEncoder):
    """ encodes items into json file"""
    def default(self, i):
        if isinstance(i, BaseItem):
            return {'name': i.name, 'description': i.description,}
        return super().default()


    
def main():
    print("Starting game -- enter your command.")
    game = Game()
    game.Load()
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
    
    