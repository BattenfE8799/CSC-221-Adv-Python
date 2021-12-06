import world

class Player():
    """ class for the player"""
    def __init__(self):
        self.__invintory = []         #what the player starts with
        self.__health_points = 100    #starts player with 100 hp
        self.location_x, self.location_y = world.starting_position  #the players location that was saved before
        self.__won = False            #whether or not the player won

    def is_alive(self):
        """checks to see if player is alive"""
        if self.__health_points <= 0:
            return False
        else:
            return True
        
    def print_inventory(self):
        """displays the player's invintory"""
        for item in self.invintory:
            print(item, '\n')
            
    #actions player can do
    def move(self, dx, dy):
        """ player moves tiles/rooms"""
        self.__location_x += dx  #the new x coord
        self.__location_y += dy  #the new y coord
        # displays the new locations intro text.
        print(world.tile_exists(self.__location_x, self.__location_y).intro_text()) 
    
    #moves the player north, south, east, or west
    def move_north(self): 
        if "North" in world.tile_exists(self.__location_x, self.__location_y).exits:
            self.move()
        
    def move_south(self): self.move(dx=0, dy=1)

    def move_east(self): self.move(dx=1, dy=0)

    def move_west(self): self.move(dx=-1, dy=0)
    
    #player attacks TODO (I dont need it)
    
    def pickup_item(self, item):
        """player picks up item and puts it into their invintory"""
        try:
            if item.__can_pickup == True:
                if item in world.tile_exists(self.__location_x, self.__location_y).__box:
                    world.tile_exists(self.__location_x, self.__location_y).__box.remove(item)
                    self.__invintory.append(item)
        except:
            print("You cannot pick that up.")
        
    def do_action(self, action, **kwargs):
        """ has the player do the action"""
        try:
            action_method = getattr(self, action.method.name) #looks for a method and stores it as an object
            if action_method: 
                action_method(**kwargs) #execute method with kwargs incase method needs additional objects like the attack method
        except:
            print("You cannot do that.")
            
        
    
    
    
    