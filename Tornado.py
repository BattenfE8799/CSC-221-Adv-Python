"""
Game attempt #4 Using a combo of what we learned in class and the tutorial
"""
invintory = ['key']

class BaseItems:
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
        
        
    
    """TODO: create if check for them to go into the shelter/puzzle"""
        
class Rooms(Containers):
    """class defining rooms """
    def __init__(self, iname, idescription, rexits):
        super().__init__(iname, idescription)
        self.exits = rexits
        
    # def __str__(self):
    #     text = f'{self.name}:\n {self.description}\n'
    #     exitList = self.exits.keys()
    #     for direction in exitList:
    #         text += direction
    #         text +=': ' + self.exits[direction]
    #         text += '\n'
    #     if self.box == {}:
    #         text += "There's no items here.\"
    #     else:
           
    #     return f'{self.name}:\n {self.description}\n In this room are: {lcontents}\n'
      
    # def get_exits(self):
    #     try:
    #         for v,k in self.exits:
    #             print(v,k)
    #     except:
            # print("There are no exits.")


class Player:
    """class detailing player"""
    def __init__(self):
        self.contents = [katie] #gives the player the invintory
        #self.location = bedroom
        
    def get_location(self):
        return self.location
    
    def set_location(self, location):
        self.location = location
        
    def add_item(self, item):
        self.contents.append(item)
        
    #player actions available
    # def move(self, direction):
    #     """decides what the players new location will be"""
    #     try:
    #         if direction in self.location.exits:
    #             self.set_location(VALUE)
    #     except:
    #         print("You cannot go that way.")
        
    #     if direction.lower() == 'north':
    #         try:
    #             i 
    #         except:
    #             print("")
    #         self.set_location() """TODO finish code changing location"""
    #     elif direction.lower() == 'south':
    #         self.set_location() """TODO finish code changing location"""
    #     elif direction.lower() == 'east':
    #         self.set_location() """TODO finish code changing location"""
    #     elif direction.lower() == 'west':
    #         self.set_location() """TODO finish code changing location"""
    
    
        
class Actions:
    """class detailing all the actions player can take"""
    pass

"""tests base items    """
pencil = BaseItems('Pencil', 'Wooden and sharp.')
print(pencil)
eraser = BaseItems('Eraser', 'Rubbery and blue')
BaseItems.print_item(eraser)

""""test doors and the locking and unlocking function of them"""
heart_door = Doors('Heart','Its a door in the shape of a heart.', True)
print(heart_door)
heart_door.unlock_door() 
print(heart_door)
heart_door.lock_door()
print(heart_door)

"""test containers list_contents of the list containing the items in the containe"""
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
aqua_box.list_contents()


"""tests npcs"""
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
katie = BaseItems('Katie', 'small, old, and sweet')
invintory.append(katie)
npc1.give_item(katie)
npc1.list_contents()

"""tests rooms with move action"""
bedroom = Rooms('Bedroom','Its your bedroom.',{'East':'bathroom', 'north':'kitchen'})
kitchen = Rooms('Kitchen','Its your kitchen.',{'south':'bedroom'})
bathroom = Rooms('Bathroom','Its your bathroom.',{'west':'bedroom'})
bathroom.box.append(gold_box)
print(bedroom)
print(bathroom)
print(kitchen)
print()
bathroom.box.append(gold_box)
bathroom.list_contents()
kitchen.list_contents()
"""test player class creation"""
# player = Player()
# print(player.get_location())
# print(player)



# class Player:
#     """class detailing player"""
#     def __init__(self):
#         self.invintory = [] #gives the player the invintory
#         self.location = Rooms.bedroom
        
#     def get_location(self):
#         return self.location
    
#     def set_location(self, location):
#         self.location = location