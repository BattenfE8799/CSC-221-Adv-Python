# CSC 221
# Text Adventure
# norrisa
# 10/1/21
from Room import Room, Door
from Container import Item, Player
import time

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

     v4- creating if statements for npcs and shelter door
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
        self.rooms = {} # stored in dictionary
        self.items = []
        # Player is currently used to hold current location (loc)
        self.player = Player("Player","You are the player.") 
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
        self.end_game = False
        

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def output(self, message):
        """ output the message. Just uses print() in base class.
        You might for example subclass to use Flask, etc. """
        print(message)

    def setup(self):
        """ sets up the game"""
        bedroom = Room('Bedroom',"Its you and your spouse's bedroom.", {"west": "Hall", "south": "Bathroom"})
        livingroom= Room("Living Room","Its the livingroom, everyone spends alot of time here.\n.", {"east": "Dining Room"})
        # papawroom= Room("Papaw's Room", "Its Papaw's bedroom.", {"north": "Living Room"})
        diningroom= Room('Dining Room',"Its where you all eat meals together.\n The cat likes sitting in the chairs.", {"west":"Living Room", "south": "Stairs", "east": "Kitchen"})
        kitchen= Room('Kitchen',"It's where the family cooks their meals. Leads to the back yard.", {"west":"Dining Room","east":"Back Yard"})
        hall= Room('Hall',"Its a hallway.", {"east":"Bedroom","south":"Stairs"})
        # nanaroom= Room("Nana's Room","It's Nana's bedroom. Child tends to spend time with her in here.", {"south":"Hall"})
        # childroom= Room("Child's Room","Its your youngest's bedroom. Your pet snake lives in here.", {"west":"Hall"})
        bathroom= Room("Bathroom","Its you and your spouse's bathroom.", {"north":"Bedroom"})
        # attic= Room('Attic',"Its where your teen hangs out.", {"south":"Stairs"})
        backyard= Room('Back Yard',"Its the back yard, the shed and shelter are here.", {"north":"Shed", "south":"Tornado Shelter"})
        shed= Room('Shed',"Your dog likes hanging out here.", {"south":"Back Yard"})
        shelter= Room('Tornado Shelter',"This is the only thing that will protech you and yours from a tornado.", {"out":"Back Yard"})
        # shelterDoor= Room('Shelter Door',"The door to the shelter, its locked. You need a key.", {"in":"Tornado Shelter","out":"Back Yard"})
        stairs = Room('Stairs',"Stairs to travel between the first and second floors.", {"down":"Dining Room", "up":"Hall"})

        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        self.rooms = { bedroom.name: bedroom,
                    livingroom.name: livingroom,
                    #papawroom.name: papawroom,
                    diningroom.name: diningroom,
                    kitchen.name: kitchen,
                    hall.name: hall,
                    #nanaroom.name: nanaroom,
                    #childroom.name: childroom,
                    bathroom.name: bathroom,
                    #attic.name: attic,
                    backyard.name: backyard,
                    shed.name: shed,
                    shelter.name: shelter,
                    stairs.name: stairs}
                    #shelterDoor.name: shelterDoor}
        
        
        # Add some items to the rooms
        shelter_key = Item("key", "Its the key that unlocks the shelter.")
        shed.addItem(shelter_key)
        #oxygen_tank = Item("oxygen", "Its Nana's oxygen tanks, she can't go anywhere without them.")
        #livingroom.addItem(oxygen_tank)
        #blanket = Item("blankey", "They won't go anywhere without it when sleepy.")
        #nanaroom.addItem(blanket)
        leash = Item("leash", "Its the dog's leash. Its the only way to get them to follow you when they're scared.")
        kitchen.addItem(leash)
        cat = Item("cat", "The family's cat. Likes to sleep on the dining room chairs.")
        diningroom.addItem(cat)
        snake = Item("snake", "Your pet snake, Snape. It doesn't mind being moved.")
        bedroom.addItem(snake)
        dog = Item("dog","Your pet dog. Its very scared.")
        backyard.addItem(dog)
        self.items = shelter_key
        
        #bird = Item("bird", "A pretty bird, that the cat tries to eat.")
        
        #add some containers
        
        #door setup
        frontDoor = Door("FrontDoor", "The door to the front yard is blocked on the outside. You can't go that way.")
        frontDoor.locked = True
        frontDoor.state = 1
        livingroom.addDoor(frontDoor, "west")
        backDoor = Door("BackDoor", "The back door.")
        backDoor.locked = False
        backDoor.state = 1
        kitchen.addDoor(backDoor, "east")        
        
        bathroomDoor = Door("BathroomDoor","The door to the bathroom.")
        bathroomDoor.locked = False
        bathroomDoor.state = 1
        bedroom.addDoor(bathroomDoor, "south")
        bathroom.addDoor(bathroomDoor, "north")
        shelterDoor = Door("ShelterDoor", "The door to the storm shelter.")
        shelterDoor.locked = True
        shelterDoor.state = 1
        backyard.addDoor(shelterDoor, "south")
        
        #getting up the gameplay startup information
        print('_'*55,'\n\n','/_'*5,"Welecome to the Tornado Game!", '_\\'*5,'\n', '_'*55,'\n')
        time.sleep(1)
        print("You wake up in your bedroom. Its noon, but dark out.\n")
        time.sleep(2)
        print("You look out the window and its just very cloudy...and windy...\n")
        time.sleep(2)
        print("BEEP BEEEP BEEEEEP BEEP\n")
        time.sleep(2)
        print("You look at your phone, its a important weather alert...\n") 
        time.sleep(2)
        print("         THERE'S A TORNADO COMING AT YOU!\n\n     ") 
        time.sleep(1)
        print("         You need to get to the storm shelter!\n\n")
        time.sleep(2)
        print('_'*55,'\n')
        time.sleep(2) 
        
    
        
        self.here = self.rooms["Bedroom"]# starting location
        # Let's do a turn 1 look , to orient the player
        self.here.describe() 
    
         

        
    def loop(self):
        """ loop(): the main game loop.
            Continues until the user quits. 
        """
        turn_counter = 1
        player = self.player
        player.contents = []
        while player.is_alive == True:
            turn_counter += 1
            if player.loc == self.rooms["Tornado Shelter"]:
                break
            if turn_counter == 15:
                print("\n\nSOUNDS LIKE A TRAIN IS COMING!\n\n I better hurry!\n")
            if turn_counter == 20:
                break
            # self.roomAction()
            self.playerAction()
        if turn_counter >= 20:
            self.ended()
        else:
            self.ending()        


    def ending(self):
        """ decides if the player won or not"""
        
                #getting up the ending gameplay information
        print('_'*55,'\n\n','/_'*8,"Thanks for Playing!", '_\\'*8,'\n', '_'*55,'\n')
        time.sleep(1)
        print("You step into the shelter and a giant gust of wind tears off the shelter door.\n")
        time.sleep(2)
        print("Its so dark it looks like night...Even though its midday\n")
        time.sleep(2)
        print("Its eerily quiet, nothing is making noise, and all the wind has stopped.\n")
        time.sleep(2)
        print("You turn to run down into the shelter....\n") 
        time.sleep(2)
        print("         WHAM!\n\n      A tree branch flys into the uncovered shelter. \n\n")
        time.sleep(2)
        print(" You died...")
        print('_'*55,'\n')
        input("Press Enter to end the program...")
        # time.sleep(2) 
        # invintory = self.player.list_contents()
        # rcontents = self.rooms['Tornado Shelter'].list_contents()
        # print("invintory: ", invintory)
        # print("room contents: ", rcontents)
        
        # if self.player.partial_win == False:
        #     print("You didn't win, the torndao took your family.\n It took you {turns_counted} turns to end the game!")
        # elif self.player.win == False:
        #     print("You didn't get everyone to safety! You lose!\n It took you {turns_counted} turns to end the game!")
        # elif self.player.partial_win == True:
        #     print("You won...technically...what about the pets?\n It took you {turns_counted} turns to end the game!")
        # elif self.player.win == True:
        #     print(f'You Won! Eveyone you love is safe from the tornado! Including your pets!\n It took you {self.turns_counted} turns to end the game!')
        # pass
        
    def ended(self):
        """Didn't make it to shelter"""
        print("The sky turns black and you hear nothing at all....\n It's eerily quiet.\n")
        time.sleep(2)    
        print("WHOOOOOOSSSHHH")
        time.sleep(2)
        print("The tornado has come. It picked you up and threw you.")
        time.sleep(2)
        print("You died. The end.")
        input("Press Enter to end the program...")
        
    def end(self):
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
        elif verb == 'inv':
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
        
        #trying again
        # item = None
        # itemName = self.items
        # print("Item:",itemName)
        # for thing in self.player.contents:
        #     print(self.player.contents)
        #     print("check1:")
        #     if thing == itemName:
        #         print("Check2:")
        #         item = thing
        #         print(item)
        #error for this one is AttributeError: 'str' object has no attribute 'unlock' line 319
        # item = None
        # itemName = 'key'
        # for thing in self.player.contents:
        #     if thing.name == itemName:
        #         item = thing
        # if item != None:
        #     print("you unlock the door.")
        #     door.unlock()
        #     door.look()
                
        # if item != None:    
        #     self.player.contents.remove(item)
        #     print ('You unlock the door.')
        #     door.unlock()
        #     door.look()
            
        # else:
        #     print(f'You dont have a {itemName} to drop!') 
        
        #error for both below wouldn't check the item
        # print("debug before checking")
        # # if self.player.contains(self.items(shelter_key) == True:
        # #     if door != None:
        # #         print("after checking")
        # #         door.unlock()
        # #         door.lock()
        # #         print('after unlocking')                
        
        # """ ***********NEED HELP UNLOCKING DOOR*******"""
        # item = None
        # for thing in self.player.contents:
        #     item = thing
        #     if item == 'key':
        #         print(item)
        #         if door != None:
        #             door.unlock()
        #             door.look()
        
        
        
        # door = self.here.door
        # item = 'item'
        # for thing in self.player.contents:
        #     if thing == 'key':
        #         item = thing
        #     if item in self.player.contents:
        #         if door != None:
        #             door.unlock()
        #             door.look()
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
