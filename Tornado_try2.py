"""
Game attempt #5 Using a combo of what we learned in class and the tutorial
--broke it and got lost trying to fix it.
--What works:
    baseitems, and thier creation, and giveing and taking
    doors,
    npcs
    containers
    --made player a container class
    
TODO:
    
"""
invintory = ['key']

class BaseItems:
    """ creats basic items in the game, also is superclass of most other classes"""
    def __init__(self, iname, idescription):
        self.name = iname
        self.description = idescription 
        
    def __str__(self):
        return f'{self.name}, {self.description}'
    
    #creating getters and setters for this information
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    
    def set_name(self, iname):
        self.name = iname
    def set_description(self, idescription):
        self.description
        
    def print_item(self):
        print(f'{self.name}: {self.description}.')
        
class Doors(BaseItems):
    """ Creates doors and gives them the locked attribtute. also has lock and unlock methods"""
    def __init__(self, iname, idescription, is_locked):
        super().__init__(iname, idescription)   #sends to/from parent class
        
        #flags whether or not its locked
        self.is_locked = is_locked
        
    def __str__(self):
        if self.is_locked == True:
            return f'{self.name} Door:\n {self.description}\n It is locked.\n'
        elif self.is_locked == False:
            return f'{self.name} Door:\n {self.description}\n It is unlocked.\n'
   
    def get_is_locked(self):
        return self.is_locked
    def set_is_locked(self, lock):
        self.is_locked = lock
    
    def unlock_door(self):
        try:
            if self.is_locked == True:
                try:
                    if 'key' in invintory:
                        self.set_is_locked(False)
                except: 
                    print("...You can't unlock a door without a key...")
        except:
            print("Why would you try to unlock an unlocked door...")
    
    def lock_door(self):
        try:
            if self.is_locked == False:
                self.set_is_locked(True)
        except:
            print("You can't lock a locked door..")

class Containers(BaseItems):
    def __init__(self, iname, idescription):
        super().__init__(iname, idescription)
        self.box = []   #creates a dictionary to contain items in the container
    
    def get_box(self):
        return self.box
        
    def list_contents(self):
        """prints items from the dictionary"""
        if self.box == []:
            print("Nothing here.")
        else:
            for item in self.box:
                print(item)

class NPC(Containers):
    """ class defineing Npcs"""
    def __init__(self, iname, idescription):
        super().__init__(iname, idescription)
        self.requirement = False #Boolean attribute that says if they are okay to go into the shelter or not
        self.puzzle = ' '
        self.puzzle_solved = False
        
    """checks the attribute"""    
    def get_requirement(self):
        return self.requirement
    def get_puzzle(self):
        return self.puzzle
    def get_puzzle_solved(self):
        return self.puzzle_solved
    """sets the attribute"""
    def set_requirement(self, req):
        self.requirement = req
    def set_puzzle_solved(self, solved):
        self.puzzle_solved = solved
    
    def give_item(self, item):
        """gives the npc an item"""
        if item in invintory:
            self.box.append(item)
            invintory.remove(item)
        else:
            print("can't do that")

class Rooms(Containers):
    """class defining rooms """
    def __init__(self, iname, idescription, rexits):
        super().__init__(iname, idescription)
        self.exits = rexits
        
        
class Player(Containers): # I put it as a subclass of containers to make it easier.
    """class detailing player"""
    def __init__(self, iname, idescription):
        super().__init__(iname, idescription)
        self.location = bedroom
        
    def __str__(self):
        itemlist = []
        for item in self.box:
            itemlist.append(item)
        if itemlist == []:
            return f"It's you...\n You have nothing with you.\n You're in your {self.location}"
        else:    
            return f"It's you...\n You have: {itemlist}.\n You're in your {self.location.name}"
        
    def get_location(self):
        return self.location
    
    def set_location(self, location):
        self.location = location
        
    def list_invintory(self):
        """prints items from the dictionary"""
        if self.contents == []:
            print("Nothing here.")
        else:
            for item in self.contents:
                print(item)
        
"""tests base items    """
print("\nStart of Base Items test:\n***************")
pencil = BaseItems('Pencil', 'Wooden and sharp.')
print(pencil)
eraser = BaseItems('Eraser', 'Rubbery and blue')
BaseItems.print_item(eraser)
print("End of Base Items test\n***************")

""""test doors and the locking and unlocking function of them"""
print("\nStarting: Door Class test\n***************")
heart_door = Doors('Heart','Its a door in the shape of a heart.', True)
print(heart_door)
heart_door.unlock_door() 
print(heart_door)
heart_door.lock_door()
print(heart_door)
print("End of: Door class test\n***************")

"""test containers list_contents of the list containing the items in the containe"""
print("\nStarting: Container Class test\n================")
gold_box = Containers('Gold Box','Its a box laid in gold') #creates instance
yellow_box = Containers('Yellow Box', 'Its a yellow box')  #creates instance
gold_box.box.append(1)          #adds 1 to list of gold box
yellow_box.box.append(2)        #adds 2 to list of yellow box
gold_box.list_contents()        #lists contents of gold box
yellow_box.list_contents()      #lists contents of yellow box
print("get gold Box: ",gold_box.get_box())   #checks if get_box method works 
yellow_box.box.append(gold_box) #checks if i can add an instance to the list (for future items)
yellow_box.list_contents()     #lists new contents of yellow box, that includes the gold box. It works. it does not list what is in the gold box tho.
aqua_box = Containers('Aqua Box', 'Its aqua and holds water.')
aqua_box.list_contents() #shows what empty list comes back as 
print("End of: Container class test\n================")


"""tests npcs"""
print("\nStarting: NPC Class test\n~~~~~~~~~~~~~~~~")
npc1 = NPC('Nana', 'nana of the game')  #creates the ncp
npc2 = NPC('Papaw', 'papaw of the game')
print(npc1) #tests the creation of the npc
print(npc2)
npc1.get_requirement() #gets the requirements of the npc (if true or false)
if npc1.requirement == False:
    print("She refuses to go to the shelter yet.")
npc2.get_requirement()
npc1.box.append('key') #adds key to their invintory
npc1.list_contents() #checks their invintory
katie = BaseItems('Katie', 'small, old, and sweet') #adds custom object into game
invintory.append(katie)  #adds object to invintory(global as of right now)
npc1.give_item(katie) #gives item object to npc1
print("Npc list with katie: ")
npc1.list_contents()
print("End of: NPC class test\n~~~~~~~~~~~~~~~~")


"""tests rooms with move action"""
print("\nStarting: NPC Class test\n---------------")
bedroom = Rooms('Bedroom','Its your bedroom.',{'East':'bathroom', 'north':'kitchen'})
kitchen = Rooms('Kitchen','Its your kitchen.',{'south':'bedroom'})
bathroom = Rooms('Bathroom','Its your bathroom.',{'west':'bedroom'})
bathroom.box.append(gold_box)
print(bedroom)
print(bathroom)
print(kitchen)
print()
bathroom.box.append(gold_box)
print("Printing lists now:")
bathroom.list_contents() #has gold box (2)
kitchen.list_contents() #as nothing
print("End of: NPC class test\n-----------------")


"""tests player class"""
print("\nStarting: player Class test\n@@@@@@@@@@@@@@@")
player = Player('Player', 'You.')
print(player.get_location())
print(player)
print("End of: NPC class test\n@@@@@@@@@@@@@@@")