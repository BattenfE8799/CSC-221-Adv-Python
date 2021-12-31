from dataclasses import dataclass
"""
v1: read and write to a file works. 
- can make instances with lines read from file.
- checks to see if item exists before appending it to file.
- appends to end of file
-- adds newline so its not all on one line
--TODO: 
    -Adjust checking if exists so it has to be exact. So health potion doesnt equal potion.
    --use word boundaries to mark names specficially
v2: fixed issue with last character disapearing, and fixed exact lookup
    
"""
@dataclass(frozen=True, order=True) #immutable with frozen =true
class Items:
    name: str
    description: str
    value: int = 0
    
    def __str__(self):
        return f'{self.name}: {self.description} Value: {self.value}'
    
    
@dataclass(frozen=True, order=True) #immutable with frozen =true
class Rooms:
    name: str
    description: str
    exits: dict
    contents: list
    
    
    def __str__(self):
        return f'{self.name} {self.description}'


def main():
       listing = []
       rooms = {}
       listing = item_setup()
       rooms = room_setup()
       if len(listing)==0:
           print("\nThere are no items in the game.\n")
       else:
           print("\nItems in game: \n")
           for item in listing:
               print(item)
       if len(rooms)==0:
           print("There are no rooms in this game.\n")
       else:
           print("Rooms in the game: \n")
           print(rooms)
            
def item_setup_adding_Items():
        numItems = int(input("How many items will you add?\n Do not use ';': "))
        for x in range(numItems):  
            with open('items.txt', 'w') as txt:
                itemname = input("Item Name: ")
                itemDescription = input("Description: ")
                itemValue = input("Item Value: ")
                item = f'\b{itemname}\b; {itemDescription}; {itemValue}'
                newName = f'\b{itemname}\b'
                there = searchItemText(newName)                       
                if there == True:
                    print("\n It's already there.\n")
                else:
                    txt.close()
                    with open('items.txt', 'a') as txt:
                        txt.write(item)
                        txt.write("\n")
                        txt.close()
 
def room_setup_adding_Rooms():
    """
    adds rooms via loops

    """
    #number of rooms to add
    numRooms = int(input("How many rooms will you add?\n Do not use ';': "))
    #for the number of rooms to add, loop
    for x in range(numRooms):  
        #open txt file each time
        with open('rooms.txt', 'r') as txt:
            #get room info
            roomName = input("Room Name: ")
            roomDescription = input("Description: ")
            numExits = int(input("How many exits will this room have?: "))
            roomExits = {}
            
            #loops for exits dictionary
            for y in range(numExits):
                #gets direction and room it exits to
                roomExitDirection = input("Room Exit direction: ")
                roomExitTo = input("Direction exits to: ")
                #puts it into dictionary
                roomExits[roomExitDirection] = f'<{roomExitTo}'
                
            #loop for room contents
            roomContents = []
            numContents = int(input("How many items go in this room?: "))
            for z in range(numContents):
                roomItem = input("Item: ")
                #check if item exists
                there = searchItemText(roomItem)
                if there == False:
                    print("You cannot add an item that doesn't exist.")
                elif there == True:
                    #use itemlist from items.py to add item to room contents
                    roomContents.append(roomItem)
            room = f'\b{roomName}\b; {roomDescription}; {roomExits}; *{roomContents}* '
            newName = f'\b{roomName}\b'
            #search through text file
            readfile = txt.read()
            print(newName)
            if newName in readfile:
                print("\n It's already there.\n")
                
            else:
                txt.close()
                with open('rooms.txt', 'a') as txt:
                    txt.write(room)
                    txt.write("\n")
                    txt.close()                        
                        
def searchItemText(newName):
    with open('items.txt', 'r') as txt:
        readfile = txt.read()
        if newName in readfile:
            return True
        else: 
            return False
def room_setup():
    room_setup_adding_Rooms()
    roomDict = {}
    exits = {}
    content = []
    with open('rooms.txt', 'r') as txt:
        for line in txt:
            name, description, exit1, contents = line.split(';')
            name = name.replace("\b","")
            exits = exit1
            # for word in exits:
            #     direction1, exit1 = word.split('<')
                #split exits and directions by < and > to help create dictionary
                # exits[direction1] = exit1
            for item in contents:
                name, description, value = line.split(';')
                name = name.replace("\b","")
                content.append(Items(name, description, value))
            
                
                
                
                
            

def item_setup():
    item_setup_adding_Items()
    listing = []
    with open('items.txt', 'r') as txt:
        for line in txt:
            name, description, value = line.split(';')
            name = name.replace("\b","")
            listing.append(Items(name, description, value))
    return listing
        
if __name__ == '__main__':
    main()

    
