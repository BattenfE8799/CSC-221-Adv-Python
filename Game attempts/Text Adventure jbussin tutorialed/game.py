import world
from player import Player
#import escape_the_tornado


def play():
    
    world.load_tiles() #loads the world tiles from file
    player = Player() #creates a new player object
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    
    while player.is_alive() and not player.victory:
        room = world.world.tile_exists(player.__location_x, player.__location_y) # room object if room exists, this is the players location
        room.modify_player(player) #modifys player location
        
        #check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input("What are you gonna do?: ")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
                
if __name__ =="__main__":
    play()
        
        