from Tornado_try2 import Rooms, Doors, NPC, Player

class Game:
    """organizes all the game data in a central location"""
    def __init__(self):
        self.rooms = {} # actually created in my game
        self.player = Player("player","Its you") #creates player
        self.playing = True
        self.turns_counted = 0
        self.win_conditions = []
        
    def setup(self):
        """creates graph of rooms for playing."""
        pass
    
    def loop(self):
        self.playing =True
        while self.playing == True:
            self.playerAction()
            self.turns_counted += 1
        print("!GAME OVER!")

    def end(self):
        """Ends the game, explaining the  turns played"""
        self.won()
        if self.player.partial_win == False:
            print("You didn't win, the torndao took your family.\n It took you {turns_counted} turns to end the game!")
        elif self.player.win == False:
            print("You didn't get everyone to safety! You lose!\n It took you {turns_counted} turns to end the game!")
        elif self.player.partial_win == True:
            print("You won...technically...what about the pets?\n It took you {turns_counted} turns to end the game!")
        elif self.player.win == True:
            print(f'You Won! Eveyone you love is safe from the tornado! Including your pets!\n It took you {self.turns_counted} turns to end the game!')
        
    def won(self):
        result = all(elem in Rooms.shelter.box for elem in GameLoader.win_conditions)
        result2 = all(elem in Rooms.shelter.box for elem in GameLoader.won_conditions)
        if result:
            self.player.win == True
        if result2:
            self.player.partial_win == True

class MyGame(Game):
    """Specific features for my game"""
    def setup(self):
        loader = GameLoader()
        self.rooms = loader.setup()
        
        #starting location
        self.here = self.rooms["Bedroom"]
        self.here.describe()
        
        
        
        
        
class GameLoader:
    """the room setup"""
    
    def setup(self):
        
        #create all the rooms as instances of the room class
        bedroom = Rooms('Your Bedroom',"Its you and your spouse's bedroom.", {"East": "Hall", "South": "Bathroom"})
        livingroom= Rooms('Livingroom',"Its the livingroom, everyone spends alot of time here.\n The bird stays in here.", {"East": "Front Yard", "South": "Papaw's Room", "West": "Dining Room"})
        papawroom= Rooms("Papaw's Room", "Its Papaw's bedroom.", {"North": "Living Room"})
        diningroom= Rooms('Dining Room',"Its where you all eat meals together.\n The cat likes sitting in the chairs.", {"South": "Stairs", "East": "Kitchen"})
        kitchen= Rooms('Kitchen',"It's where the family cooks their meals. Leads to the back yard.", {"East":"Dining Room","West":"Back Yard"})
        hall= Rooms('Hall',"Its a hallway.", {"East":"Child's Room","North":"Nana's Room","West":"My Bedroom","South":"Stairs"})
        nanaroom= Rooms("Nana's Bedroom","It's Nana's bedroom. Child tends to spend time with her in here.", {"South":"Hall"})
        childroom= Rooms("Child's Bedroom","Its your youngest's bedroom. Your pet snake lives in here.", {"West":"Hall"})
        bathroom= Rooms('Your Bathroom',"Its you and your spouse's bathroom.", {"North":"Bedroom"})
        attic= Rooms('The Attic',"Its where your teen hangs out.", {"South":"Stairs"})
        frontyard= Rooms('Front Yard',"Its the front yard, its been recently mowed.", {"North":"Side Yard","West":"Living Room"})
        sideyard= Rooms('Side Yard',"Its the side yard, its filled with papaw's flowers.", {"South":"Side Yard","West":"Back Yard"})
        backyard= Rooms('Back Yard',"Its the back yard, the shed and shelter are here.", {"East":"Side Yard","North":"Shed", "South":"Shelter"})
        shed= Rooms('Shed',"Your dog likes hanging out here.", {"South":"Back Yard"})
        shelter= Rooms('Tornado Shelter',"This is the only thing that will protech you and yours from a tornado.", {"North":"Back Yard"})

        #the rooms are in a dictionary
        roomDict = { bedroom.name: bedroom,
                    livingroom.name: livingroom,
                    papawroom.name: papawroom,
                    diningroom.name: diningroom,
                    kitchen.name: kitchen,
                    hall.name: hall,
                    nanaroom.name: nanaroom,
                    childroom.name: childroom,
                    bedroom.name: bedroom,
                    bathroom.name: bathroom,
                    attic.name: attic,
                    frontyard.name: frontyard,
                    backyard.name: backyard,
                    sideyard.name: sideyard,
                    shed.name: shed,
                    shelter.name: shelter}
        
        return roomDict
        #adds items to the rooms for the game 
    
    def items_setup(self):
        key = BasicItem("Shelter Key", "Its the key that unlocks the shelter.")
        
    
        #adds items to the npcs for the game
    def npc_setup(self):
        """sets up the nps, what they hold, what they need"""
        nana = NPC('Nana', "Your mom, she need her oxygen to go anywhere.\n She can't be near Papaw.")
        papaw = NPC('Papaw', "Your dad. He just had laser eye surgery and can't see yet.\n He can't be near nana.")
        spouse = NPC('Spouse', "Your spouse.\nNeeds the kids saved first.")
        child  = NPC('Child', "Your youngest, a todler that is too sleepy to walk.\n Needs their blanket to go anywhere.")
        teen = NPC('Teen', "Your eldest. Cranky with a broken hand. Stuck their other hand in a pickle car.Can't carry anything.\n Needs the dog safe to go in the shelter.")
        dog = NPC('Dog', "Your family's dog, its too scared to move, it needs the leash.")
        cat = NPC('Cat', "Your family's cat\n She'll eat the bird if left alone with it.")
        snake = NPC('Snake', "Your pet snake, its just fine being moved around.")
        bird = NPC('Bird', "Your family's bird, it needs to be in the cage to go anywhere\n It can't be left with the cat.")
        
        teen.give_item(key.BasicItems)
    def win_conditions(self):
        """sets up the win conditions"""
        win_list = [] #the list that the shelter list has to include to win or partially win.
    def won_conditions(self):
        """sets up the almost win conditions"""
        won_list = []
    
#starts up the game:
def main():
    game = MyGame()
    game.setup()
    game.output("Ready to play? Enter a command!")
    game.loop()
    game.end()

if __name__ == "__main__":
    main()    