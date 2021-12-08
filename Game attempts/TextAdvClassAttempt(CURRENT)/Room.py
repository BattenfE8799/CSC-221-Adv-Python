# CSC 221
# M3T1- Text Adventure-5Rooms with descriptions
# Elizabeth Battenfield
# 10/18/21

from Container import Container, Item, Player

class Room(Container):
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    """

        
    def __init__(self, name, description, exits):
        super().__init__(name, description)
        self.exits = exits # First pass at items in rooms
        self.door = None
        self.lockedexit = None

    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        #adds name and description

        
        # text = '\n'+ self.name + ":" + "\n"
        # text += self.description + "\n\n" + "Exits: \n"
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

 #   def __repr__(self):  # we're not using this yet
 #       pass


    def describe(self):
        """ print full room description. """
        print(self)
    
    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
        # I need access to the roomDict for this -- so it should 
        # go in Game, not Room.             
            
    def addItem(self, item):
        """ used to add an item into a room. """
        self.contents.append(item)
    
    def removeItem(self, item):
        """ used to remove items from a room. """
        if item in self.contents:
            self.remove(item)
    
    def addDoor(self, door, lockedexit):
        self.door = door
        self.lockedexit = lockedexit
        
class Door():
    def __init__(self, name, description, state, locked):
        self.name = name
        self.description = description
        self.state = state
        self.locked = locked
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

