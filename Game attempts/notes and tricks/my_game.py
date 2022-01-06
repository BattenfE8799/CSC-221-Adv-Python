# -*- coding: utf-8 -*-
"""
My game for game engine
v1- useing json to load data
 --Creating my specific rooms and items
 
"""
from dataclasses import dataclass #enables use of dataclass
import json                       #import json to use json objects and files
from gameSetup import BaseItem, Container, Player, Game, Room, ItemEncoder, Door
import sys #to quit game

class My_Game(Game):
    def __init__(self):
        super().__init__()
        self.roomItems = {}
    
    def setup(self):
        """sets up rooms, items etc"""
        bedroom = Room('Bedroom',"Its you and your spouse's bedroom.",[],  {"west": "Hall", "south": "Bathroom"})
        livingroom= Room("Living Room","Its the livingroom, everyone spends alot of time here.\n.",[],  {"east": "Dining Room"})
        papawroom= Room("Papaw's Room", "Its Papaw's bedroom.",[],  {"north": "Living Room"})
        diningroom= Room('Dining Room',"Its where you all eat meals together.\n The cat likes sitting in the chairs.", [], {"west":"Living Room", "south": "Stairs", "east": "Kitchen"})
        kitchen= Room('Kitchen',"It's where the family cooks their meals. Leads to the back yard.",[],  {"west":"Dining Room","east":"Back Yard"})
        hall= Room('Hall',"Its a hallway.",[],  {"east":"Bedroom","south":"Stairs"})
        nanaroom= Room("Nana's Room","It's Nana's bedroom. Child tends to spend time with her in here.",[],  {"south":"Hall"})
        childroom= Room("Child's Room","Its your youngest's bedroom. Your pet snake lives in here.",[],  {"west":"Hall"})
        bathroom= Room("Bathroom","Its you and your spouse's bathroom.",[],  {"north":"Bedroom"})
        attic= Room('Attic',"Its where your teen hangs out.",[],  {"south":"Stairs"})
        backyard= Room('Back Yard',"Its the back yard, the shed and shelter are here.", [], {"north":"Shed", "south":"Tornado Shelter"})
        shed= Room('Shed',"Your dog likes hanging out here.", [], {"south":"Back Yard"})
        shelter= Room('Tornado Shelter',"This is the only thing that will protech you and yours from a tornado.", [], {"out":"Back Yard"})
        shelterDoor= Room('Shelter Door',"The door to the shelter, its locked. You need a key.",[],  {"in":"Tornado Shelter","out":"Back Yard"})
        stairs = Room('Stairs',"Stairs to travel between the first and second floors.",[],  {"down":"Dining Room", "up":"Hall"})
        
        # roomsList = [bedroom = Room('Bedroom',"Its you and your spouse's bedroom.",[], {"west": "Hall", "south": "Bathroom"}), 
        #             livingroom= Room("Living Room","Its the livingroom, everyone spends alot of time here.\n.",[], {"east": "Dining Room"}),
        #             papawroom= Room("Papaw's Room", "Its Papaw's bedroom.", [],{"north": "Living Room"}),
        #             diningroom= Room('Dining Room',"Its where you all eat meals together.\n The cat likes sitting in the chairs.",[], {"west":"Living Room", "south": "Stairs", "east": "Kitchen"}),
        #             kitchen= Room('Kitchen',"It's where the family cooks their meals. Leads to the back yard.",[], {"west":"Dining Room","east":"Back Yard"}),
        #             hall= Room('Hall',"Its a hallway.",[], {"east":"Bedroom","south":"Stairs"}),
        #             nanaroom= Room("Nana's Room","It's Nana's bedroom. Child tends to spend time with her in here.", [],{"south":"Hall"}),
        #             childroom= Room("Child's Room","Its your youngest's bedroom. Your pet snake lives in here.",[], {"west":"Hall"}),
        #             bathroom= Room("Bathroom","Its you and your spouse's bathroom.", [],{"north":"Bedroom"}),
        #             attic= Room('Attic',"Its where your teen hangs out.",[],{"south":"Stairs"}),
        #             backyard= Room('Back Yard',"Its the back yard, the shed and shelter are here.",[], {"north":"Shed", "south":"Tornado Shelter"}),
        #             shed= Room('Shed',"Your dog likes hanging out here.", [],{"south":"Back Yard"}),
        #             shelter= Room('Tornado Shelter',"This is the only thing that will protech you and yours from a tornado.", [],{"out":"Back Yard"}),
        #             shelterDoor= Room('Shelter Door',"The door to the shelter, its locked. You need a key.",[], {"in":"Tornado Shelter","out":"Back Yard"}),
        #             stairs = Room('Stairs',"Stairs to travel between the first and second floors.",[], {"down":"Dining Room", "up":"Hall"})]
        
        
        self.roomsItems = {"bedroom": "key"}, {"bathroom": "tp"}
        
        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        self.rooms = { bedroom.name: bedroom,
                    livingroom.name: livingroom,
                    papawroom.name: papawroom,
                    diningroom.name: diningroom,
                    kitchen.name: kitchen,
                    hall.name: hall,
                    nanaroom.name: nanaroom,
                    childroom.name: childroom,
                    bathroom.name: bathroom,
                    attic.name: attic,
                    backyard.name: backyard,
                    shed.name: shed,
                    shelter.name: shelter,
                    stairs.name: stairs,
                    shelterDoor.name: shelterDoor}
        
        
        # Add some items to the rooms
        shelter_key = BaseItem("key", "Its the key that unlocks the shelter.")
        shed.addItem(shelter_key)
        oxygen_tank = BaseItem("oxygen", "Its Nana's oxygen tanks, she can't go anywhere without them.")
        livingroom.addItem(oxygen_tank)
        blanket = BaseItem("blankey", "They won't go anywhere without it when sleepy.")
        nanaroom.addItem(blanket)
        leash = BaseItem("leash", "Its the dog's leash. Its the only way to get them to follow you when they're scared.")
        kitchen.addItem(leash)
        cat = BaseItem("cat", "The family's cat. Likes to sleep on the dining room chairs.")
        diningroom.addItem(cat)
        snake = BaseItem("snake", "Your pet snake, Snape. It doesn't mind being moved.")
        bedroom.addItem(snake)
        dog = BaseItem("dog","Your pet dog. Its very scared.")
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
        
        self.here = self.rooms["Bedroom"]# starting location
        # Let's do a turn 1 look , to orient the player
        self.here
        
    def intro(self):
        text = """
        Intro to my game
        """
        
    def title(self):
        text = """GAME TITLE"""
        
    def menu(self):
        text = """        1. Read Instructions
        2. Play New Game
        3. Load Previous Game
        4. Save Game
        5. Quit Game
        """
        while True:
            try:
                choice = int(input(text))
                break
            except ValueError:
                print("Invalid choice!")
        if choice == 1:
            self.Instructions()
        if choice ==2:
            self.Play()
        if choice ==3:
            self.Load()
        if choice ==4:
            self.Save()
        if choice ==5:
            Game.quit()
            
        
    def loop(self):
        """game loop"""
        turn_counter = 0
        player = self.player
        print(self.title)
        print(self.intro)
        self.menu()
        self.here.describe()
        while player.is_alive == True:
            win = player.win
            if win == True:
                break
            turn_counter += 1
            self.playerAction()
        self.end()
                
    def Play(self):
        pass
    
    def Instructions(self):
        text = """
        To win: Get your family and pets to safety.
        Each family member has something you must get or do to get them to safety.
        """
        print(text)
        self.menu()
        
    
    def Load(self):
        with open ('save.json', 'r') as save_file:
            data = json.load(save_file)
            # Game.roomsList = data["rooms_contents"]
            # Game.items = data["items"]
            # Game.doors = data["doors"]
            here = data["player_loc"]
            self.here = here
            print("Game Loaded")
                
    
    
    def Save(self,filename="save.json"):
        with open (filename, 'w') as f:
            here = self.here.name
            print(here)
            data = [ 
            # {"room_items": self.},
                    # {"rooms_doors": Game.roomsDoors},
                    # {"player_items": self.player.contents},
                    {"player_loc": here}]
            
            #save room contents
            file = json.load(f)
            temp = data["player_loc"]
            
            temp.append(data)
            #save room door states
            #save player stats
        print(data)
        print("game saved")
        self.menu()
    
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
        elif verb == 'menu':
            self.menu()
        else: # first word is verb
            print("I don't know how to", words[0])
# def write_json(data, filename="01_names.json"):
#     with open (filename, 'w') as f:
#         json.dump(data, f, indent = 4)
        
# with open ("01_names.json") as json_file:
#     data = json.load(json_file)
#     temp = data["names"]
#     y = {"firstname": "joe", "age" : 40}
#     temp.append(y)
    
# write_json(data)
def main():
    print("Starting game -- enter your command.")
    game = My_Game()
    game.setup()
    game.loop()
    game.end()
    
if __name__ == '__main__':
    main()
    
    
    
    # shelter_key = BaseItem("key", "Its the key that unlocks the shelter.")
    # bedroom = Room('Bedroom',"Its you and your spouse's bedroom.", [], {"west": "Hall", "south": "Bathroom"})
    # player = Game.here
    # rooms = [bedroom]
    # items = [shelter_key]
    # #pass item into  saveitems to turn into json data
    # Save(rooms, items, player)
    # Load()
    # list, tuple = array
    #dict =object
    #str = string
    #int, float = number
    #True and False = true and false
    #none = null
    
