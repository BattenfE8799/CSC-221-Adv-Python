# Item class

invintory = ['key'] #global because I can't figure it out rn

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
    """ ingerits from base Item, to create items"""
    pass

class Doors(BaseItem):
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

     

# Test code
def main():
    """tests base items    """
    print("\nStart of Base Items test:\n***************")
    pencil = BaseItem('Pencil', 'Wooden and sharp.')
    print(pencil)
    eraser = BaseItem('Eraser', 'Rubbery and blue')
    print(eraser)
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
        
if __name__ == "__main__":
    main()
