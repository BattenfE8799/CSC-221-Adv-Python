# Container class
# should be able to add, remove, list, and 
# (optionally) transfer items
#
# we moved using a dictionary so we can easily
# do name lookups

# import Game
class BaseItem:
    """
    Items are found in rooms, or in the player inventory.
    (Possibly we'll change that to being found in Container objects?)
     
    They may be used to solve puzzles, give points to score, etc.
    """
     
    def __init__(self, name, description):
         self.name = name
         self.description = description
         
    def __str__(self):
        return self.name + " : " + self.description
        
class Item(BaseItem):
    """ inherits from base Item, to create items"""
    pass




class Container(Item):
    """ This class only handles collections of Items. """
    
    def __init__(self, name, description):
        super().__init__(name, description)
        self.contents = []
        


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
    
        

  
    def contains(self, itemName):
        """ quick way to check if item is present. """
        if itemName in self.contents:
            return True
        else:
            return False

class Player(Container):
    """
    Any data relating to the player himself should go in the 
    Player class.
    """
    
    def __init__(self, name, description):
        super().__init__(name, description)
        self.loc = None # what room is the player in?
        self.contents = [] # because we're also a container
        self.win = False
        self.partial_win = False
        self.is_alive = True
        
    def __str__(self):
        pass

 
        
# def main():
#     """ test code"""
#     """test containers list_contents of the list containing the items in the containe"""
#     print("\nStarting: Container Class test\n================")
#     gold_box = Container('Gold Box','Its a box laid in gold') #creates instance
#     yellow_box = Container('Yellow Box', 'Its a yellow box')  #creates instance
#     gold_box.contents.append(1)          #adds 1 to list of gold box
#     yellow_box.contents.append(2)        #adds 2 to list of yellow box
#     gold_box.list_contents()        #lists contents of gold box
#     yellow_box.list_contents()      #lists contents of yellow box
#     print("get gold Box: ")   #checks if get_box method works 
#     yellow_box.contents.append(gold_box) #checks if i can add an instance to the list (for future items)
#     yellow_box.list_contents()     #lists new contents of yellow box, that includes the gold box. It works. it does not list what is in the gold box tho.
#     aqua_box = Container('Aqua Box', 'Its aqua and holds water.')
#     aqua_box.list_contents() #shows what empty list comes back as 
#     print("checking ability to see if something is contianed in box:")
#     print(yellow_box.contains(gold_box))
#     print(aqua_box.contains(gold_box))
#     print("End of: Container class test\n================")
    
 
    
 
# if __name__ == "__main__":
#     main()
     
     
     