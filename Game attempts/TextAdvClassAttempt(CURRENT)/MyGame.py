# MyGame - implements game specific functions
from Game import Game
from Room import Room, Door
from Item import Item
import time
""" Getting rid of this and just using Game file
"""


class MyGame(Game):
    """ the Game class should be subclassed to add
    game specific features, including the world setup. 
    """
    
    def setup(self):
        """ Load your own rooms in the method of your choosing.
        Consider a GameLoader class that might read these
        from a file...
        """
        loader = MyGameLoader()
        self.rooms = loader.setup()
    
        
        # starting location
        self.here = self.rooms["Back Yard"]
        # Let's do a turn 1 look , to orient the player
        # print("before describe")
        self.here.describe()
        # print("after decribe")

    def loop(self):
        """ loop(): the main game loop.
            Continues until the user quits. 
        """
        
        player = self.player
        player.contents = ['oxygen', 'key', 'dog']
        while player.is_alive == True:
            print(player.loc.name)
            if player.loc == self.rooms["Tornado Shelter"]:
                break
            # self.roomAction()
            self.playerAction()
     
            
        print("Game over, thanks for playing")
        self.ending()



    


    def ending(self):
        """ decides if the player won or not"""
        invintory = self.player.list_contents()
        rcontents = self.rooms['Tornado Shelter'].list_contents()
        print("invintory: ", invintory)
        print("room contents: ", rcontents)
        # if self.player.partial_win == False:
        #     print("You didn't win, the torndao took your family.\n It took you {turns_counted} turns to end the game!")
        # elif self.player.win == False:
        #     print("You didn't get everyone to safety! You lose!\n It took you {turns_counted} turns to end the game!")
        # elif self.player.partial_win == True:
        #     print("You won...technically...what about the pets?\n It took you {turns_counted} turns to end the game!")
        # elif self.player.win == True:
        #     print(f'You Won! Eveyone you love is safe from the tornado! Including your pets!\n It took you {self.turns_counted} turns to end the game!')
        # pass
    
    def end(self):
        pass
        
    # def roomAction(self):
    #     """checks any specifics needed for a room. ie:shelter needs key"""
    #     if self.here == self.rooms["Shelter Door"]:
            
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
        # if self.here.exits.get(direction) == None:
        #     print("You can't go that way.")
        # else:   
        #     # this key does exist
        #     #original start
        #     # newRoomName = self.here.exits[direction]
        #     # newRoom     = self.rooms[newRoomName]
        #     # self.here   = newRoom
        #     # if self.isVerbose:
        #     #     self.here.describe()
        #     #original end
        #     newRoomName = self.here.exits[direction]
        #     newRoom     = self.rooms[newRoomName]
        #     if newRoom == self.rooms["Tornado Shelter"]:
        #         item = None
        #         for thing in self.player.contents:
        #             if thing.name == 'key':
        #                 item = 'key'
        #         if item != None:
        #             print("You cannot enter the Shelter without the key!")
        #             newRoom = self.here
            
        #     self.here   = newRoom
        #     if self.isVerbose:
        #         self.here.describe()
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            # newRoomName = self.here.exits[direction]
            newRoomName = self.here.exits[direction]
            # print(self.rooms)
            newRoom     = self.rooms[newRoomName]
            
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()        
        
        
        
        
        
    
    def commandGet(self, itemName):
        """ remove the item from the room (if it's there)
        and place it in player inventory.
        """
        print (f'You try to get the {itemName}.')

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
        
        print("You try to drop the", itemName)
        item = None
        for thing in self.player.contents:
            if thing.name == itemName:
                item = thing
                
        if item != None:    
            self.here.contents.append(item), self.player.contents.remove(item)
            print (f'You drop the {itemName}.')
            
        else:
            print(f'You dont have a {itemName} to drop!')  


    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player.loc
    
    @here.setter
    def here(self, room):
        self.player.loc = room
    
    
    
    
    
    

    
# class MyGameLoader:
#     """ just used to put all the room setup in a separate class,
#     and if needed, a separate file.
#     """

#     def setup(self):
#         bedroom = Room('Bedroom',"Its you and your spouse's bedroom.", {"east": "Hall", "south": "Bathroom"})
#         livingroom= Room("Living Room","Its the livingroom, everyone spends alot of time here.\n The bird stays in here.", {  "south": "Papaw's Room", "west": "Dining Room"})
#         papawroom= Room("Papaw's Room", "Its Papaw's bedroom.", {"north": "Living Room"})
#         diningroom= Room('Dining Room',"Its where you all eat meals together.\n The cat likes sitting in the chairs.", {"south": "Stairs", "east": "Kitchen"})
#         kitchen= Room('Kitchen',"It's where the family cooks their meals. Leads to the back yard.", {"east":"Dining Room","west":"Back Yard"})
#         hall= Room('Hall',"Its a hallway.", {"east":"Child's Room","north":"Nana's Room","west":"Bedroom","south":"Stairs"})
#         nanaroom= Room("Nana's Room","It's Nana's bedroom. Child tends to spend time with her in here.", {"south":"Hall"})
#         childroom= Room("Child's Room","Its your youngest's bedroom. Your pet snake lives in here.", {"west":"Hall"})
#         bathroom= Room("Bathroom","Its you and your spouse's bathroom.", {"north":"Bedroom"})
#         attic= Room('Attic',"Its where your teen hangs out.", {"south":"Stairs"})
#         backyard= Room('Back Yard',"Its the back yard, the shed and shelter are here.", {"east":"Side Yard","north":"Shed", "south":"Shelter Door"})
#         shed= Room('Shed',"Your dog likes hanging out here.", {"south":"Back Yard"})
#         shelter= Room('Tornado Shelter',"This is the only thing that will protech you and yours from a tornado.", {"out":"Shelter Door"})
#         shelterDoor= Room('Shelter Door',"The door to the shelter, its locked. You need a key.", {"in":"Tornado Shelter","out":"Back Yard"})
#         stairs = Room('Stairs',"These stairs go all the way up the house into the attic...or you can get off at the second floor.", {"south":"Dining Room", "north":"Attic","east":"Hall"})

        
#         # Place rooms in a dictionary.
#         # (Game will handle this in the full version)
#         rooms = { bedroom.name: bedroom,
#                     livingroom.name: livingroom,
#                     papawroom.name: papawroom,
#                     diningroom.name: diningroom,
#                     kitchen.name: kitchen,
#                     hall.name: hall,
#                     nanaroom.name: nanaroom,
#                     childroom.name: childroom,
#                     bathroom.name: bathroom,
#                     attic.name: attic,
#                     backyard.name: backyard,
#                     shed.name: shed,
#                     shelter.name: shelter,
#                     stairs.name: stairs,
#                     shelterDoor.name: shelterDoor}
        
        
#         # Add some items to the rooms
#         shelter_key = Item("key", "Its the key that unlocks the shelter.")
#         attic.addItem(shelter_key)
#         oxygen_tank = Item("oxygen", "Its Nana's oxygen tanks, she can't go anywhere without them.")
#         livingroom.addItem(oxygen_tank)
#         blanket = Item("blankey", "They won't go anywhere without it when sleepy.")
#         nanaroom.addItem(blanket)
#         leash = Item("leash", "Its the dog's leash. Its the only way to get them to follow you when they're scared.")
#         kitchen.addItem(leash)
#         cat = Item("cat", "The family's cat. Likes to sleep on the dining room chairs.")
#         diningroom.addItem(cat)
#         snake = Item("snake", "Your pet snake, Snape. It doesn't mind being moved.")
#         bedroom.addItem(snake)
#         bird = Item("bird", "A pretty bird, that the cat tries to eat.")
#         key = Item("key","key")
#         backyard.addItem(key)
        
#         #getting up the gameplay startup information
#         print('_'*55,'\n\n','/_'*5,"Welecome to the Tornado Game!", '_\\'*5,'\n', '_'*55,'\n')
#         # time.sleep(1)
#         print("You wake up in your bedroom. Its noon, but dark out.\n")
#         # time.sleep(2)
#         print("You look out the window and its just very cloudy...and windy...\n")
#         # time.sleep(2)
#         print("BEEP BEEEP BEEEEEP BEEP\n")
#         # time.sleep(2)
#         print("You look at your phone, its a important weather alert...\n") 
#         # time.sleep(3)
#         print("         THERE'S A TORNADO COMING AT YOU!\n\n      You need to get to the storm shelter!\n\n")
#         # time.sleep(3)
#         print('_'*55,'\n')
#         # time.sleep(3)
#         return rooms 
        
        
        
# Startup
def main():
    game = MyGame()
    game.setup()
    game.output("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()

