# Item class

invintory = ['key'] #global because I can't figure it out rn
from Container import Container
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

     

# # Test code
# def main():
#     """tests base items    """
#     print("\nStart of Base Items test:\n***************")
#     pencil = BaseItem('Pencil', 'Wooden and sharp.')
#     print(pencil)
#     eraser = BaseItem('Eraser', 'Rubbery and blue')
#     print(eraser)
#     print("End of Base Items test\n***************")
        
#     """"test doors and the locking and unlocking function of them"""
#     print("\nStarting: Door Class test\n***************")
#     heart_door = Doors('Heart','Its a door in the shape of a heart.', True)
#     print(heart_door)
#     heart_door.unlock_door() 
#     print(heart_door)
#     heart_door.lock_door()
#     print(heart_door)
#     print("End of: Door class test\n***************")
        
# if __name__ == "__main__":
#     main()
