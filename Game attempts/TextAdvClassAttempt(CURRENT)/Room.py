# CSC 221
# M3T1- Text Adventure-5Rooms with descriptions
# Elizabeth Battenfield
# 10/18/21

from Container import Container
import Item

class Room(Container):
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    """

        
    def __init__(self, name, description, exits):
        super().__init__(name, description)
        self.exits = exits # First pass at items in rooms

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
            text += "Nothing you need in here."
        else:
            listcontents = self.list_contents()
            text += listcontents
            
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
    



def main():

    #Currently used for testing.
    #TODO: uimplement doctests. 
    bedroom = Room( "Bedroom", 
                   "This is a simple bedroom with a comfy bed.",
                   { "South": "Living Room"} )
    
    print(bedroom)
    
    livingRoom = Room ( "Living Room",
                       "A simple living room with a couch and TV.",
                       { "North" : "Bedroom" ,
                         "South" : "Front Yard",
                         "East"  : "Kitchen"} )
    print(livingRoom)
    
    frontYard = Room ( "Front Yard",
                       "A tidy front yard with lots of flowers.",
                       { "North" : "Living Room" } )
    print(frontYard)
    
    kitchen = Room ( "Kitchen",
                       "A kitchen themed with roosters...they're everywhere.",
                       { "North" : "Back Yard",
                         "East"  : "Living Room"} )
    print(kitchen)
    
    backYard = Room ( "Back Yard",
                       "A messy back yard, it needs to be mowed.",
                       { "South" : "Kitchen" } )
    print(backYard)    
    
    
    
    
    
    # Place rooms in a dictionary.
    # (Game will handle this in the full version)
    roomDict = { bedroom.name: bedroom, 
                livingRoom.name: livingRoom,
                frontYard.name: frontYard,
                kitchen.name: kitchen,
                backYard.name: backYard}
    # Test out items
    key = Item.Item("key", "It's a bit rusty.")
    sword = Item.Item("sword", "It's very shiny.")
    bedroom.addItem(key)
    livingRoom.addItem(sword)
    #print(loc.contents) # just dump the list
    
    # Test out movement
    loc = bedroom
    print("Starting room:")
    loc.describe()

    print ("Heading South...")
    loc = roomDict[loc.exits["South"]] # find room to South, go there
    loc.describe()
    
    print ("Heading North...")
    loc = roomDict[loc.exits["North"]] # find room to North, go there
    loc.describe()
    

    
    

if __name__ == "__main__":
    main()
