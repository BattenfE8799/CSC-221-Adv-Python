# MyGame - implements game specific functions
from Game import Game
from Room import Room
from Item import Item
import time



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
        self.here = self.rooms["Bedroom"]
        # Let's do a turn 1 look , to orient the player
        self.here.describe()
        
        
    
        
    
    
    
    
    
class MyGameLoader:
    """ just used to put all the room setup in a separate class,
    and if needed, a separate file.
    """
    def setup(self):
        bedroom = Room('Bedroom',"Its you and your spouse's bedroom.", {"east": "Hall", "south": "Bathroom"})
        livingroom= Room("Livingroom","Its the livingroom, everyone spends alot of time here.\n The bird stays in here.", {"east": "Front Yard", "south": "Papaw's Room", "West": "Dining Room"})
        papawroom= Room("Papaw's Room", "Its Papaw's bedroom.", {"north": "Living Room"})
        diningroom= Room('Dining Room',"Its where you all eat meals together.\n The cat likes sitting in the chairs.", {"south": "Stairs", "rast": "Kitchen"})
        kitchen= Room('Kitchen',"It's where the family cooks their meals. Leads to the back yard.", {"east":"Dining Room","west":"Back Yard"})
        hall= Room('Hall',"Its a hallway.", {"east":"Child's Room","north":"Nana's Room","west":"Bedroom","south":"Stairs"})
        nanaroom= Room("Nana's Room","It's Nana's bedroom. Child tends to spend time with her in here.", {"south":"Hall"})
        childroom= Room("Child's Room","Its your youngest's bedroom. Your pet snake lives in here.", {"west":"Hall"})
        bathroom= Room("Bathroom","Its you and your spouse's bathroom.", {"north":"Bedroom"})
        attic= Room('Attic',"Its where your teen hangs out.", {"south":"Stairs"})
        frontyard= Room('Front Yard',"Its the front yard, its been recently mowed.", {"north":"Side Yard","west":"Living Room"})
        sideyard= Room('Side Yard',"Its the side yard, its filled with papaw's flowers.", {"wouth":"Side Yard","west":"Back Yard"})
        backyard= Room('Back Yard',"Its the back yard, the shed and shelter are here.", {"east":"Side Yard","north":"Shed", "south":"Tornado Shelter"})
        shed= Room('Shed',"Your dog likes hanging out here.", {"south":"Back Yard"})
        shelter= Room('Tornado Shelter',"This is the only thing that will protech you and yours from a tornado.", {"north":"Back Yard"})
        stairs = Room('Stairs',"These stairs go all the way up the house into the attic...or you can get off at the second floor.", {"south":"Dining Room", "north":"Attic"})

        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        rooms = { bedroom.name: bedroom,
                    livingroom.name: livingroom,
                    papawroom.name: papawroom,
                    diningroom.name: diningroom,
                    kitchen.name: kitchen,
                    hall.name: hall,
                    nanaroom.name: nanaroom,
                    childroom.name: childroom,
                    bathroom.name: bathroom,
                    attic.name: attic,
                    frontyard.name: frontyard,
                    backyard.name: backyard,
                    sideyard.name: sideyard,
                    shed.name: shed,
                    shelter.name: shelter,
                    stairs.name: stairs}
        
        # Add some items to the rooms
        shelter_key = Item("Shelter Key", "Its the key that unlocks the shelter.")
        attic.addItem(shelter_key)
        oxygen_tank = Item("Oxygen Tanks", "Its Nana's oxygen tanks, she can't go anywhere without them.")
        livingroom.addItem(oxygen_tank)
        blanket = Item("Child's Blanket", "They won't go anywhere without it when sleepy.")
        nanaroom.addItem(blanket)
        leash = Item("Dog's Leash", "Its the dog's leash. Its the only way to get them to follow you when they're scared.")
        kitchen.addItem(leash)
        cat = Item("Cat", "The family's cat. Likes to sleep on the dining room chairs.")
        diningroom.addItem(cat)
        snake = Item("snake", "Your pet snake, Snape. It doesn't mind being moved.")
        bedroom.addItem(snake)
        bird = Item("Bird", "A pretty bird, that the cat tries to eat.")
        frontyard.addItem(bird)
        key = Item("key","key")
        bedroom.addItem(key)
        
        #getting up the gameplay startup information
        print('_'*55,'\n\n','/_'*5,"Welecome to the Tornado Game!", '_\\'*5, '_'*55,'\n')
        #time.sleep(1)
        print("You wake up in your bedroom. Its noon, but dark out.\n")
        #time.sleep(2)
        print("You look out the window and its just very cloudy...and windy...\n")
        #time.sleep(2)
        print("BEEP BEEEP BEEEEEP BEEP\n")
        #time.sleep(2)
        print("You look at your phone, its a important weather alert...\n") 
        #time.sleep(3)
        print("         THERE'S A TORNADO COMING AT YOU!\n\n      You need to get to the storm shelter!\n\n")
        #time.sleep(3)
        print('_'*55,'\n')
        #time.sleep(3)
        return rooms 
        
        
        
# Startup
def main():
    game = MyGame()
    game.setup()
    game.output("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()

