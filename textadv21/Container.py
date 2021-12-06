# Container class
# should be able to add, remove, list, and 
# (optionally) transfer items
#
# we moved using a dictionary so we can easily
# do name lookups
from Item import Item
# import Game
class Container(Item):
    """ This class only handles collections of Items. """
    
    def __init__(self, name, description):
        super().__init__(name, description)
        self.contents = []
        
    # def add(self, item):
    #     self.contents.append(item)
        
    # def remove(self, item):
    #     if item in self.contents:
    #         self.contents.remove(item)
    #         # remove the item from the dictionary
    #         # del self.contents[item.name]
    
    # def give_item(self, item):
    #     """gives the npc an item"""
    #     if item in Game.player.contents():
    #         self.contents.append(item)
    #         Game.player.contents.remove(item)
    #         print("You pick up the ",item,".")
    #     else:
    #         print("You can't see any", item, "here.")
            
    # def get_items(self, item):
    #     if item in self.here.contents:
    #         self.contents.remove(item)
    #         Game.player.contents.append(item)
    
    # def moveItemTo(self, item, destination):
        
    #     destination.append(item)
    #     self.remove(item)

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
    
        
    # i turned it from dictionary to list
    # def listContents(self):
    #     text = ""
    #     for key in self.contents:
    #         text += key 
    #         text += " : " 
    #         text += self.contents[key].description
    #         text += "\n"
    #     return text
  
    def contains(self, itemName):
        """ quick way to check if item is present. """
        if itemName in self.contents:
            return True
        else:
            return False
        # # keys() gives us a list of names of items present
        # itemNameList = []
        # for itemName in self.contents.keys():
        #     itemNameList.append(itemName)
        # print(itemNameList)
        # itemNameList = list(self.contents.keys())
        # #print(itemNameList)
        # if itemName in itemNameList:
        #     return True
        # else:
        #     return False

 
        
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
     
     
     