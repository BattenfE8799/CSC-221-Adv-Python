import game
_world = {}
starting_position = (0, 0)

def play():
    load_tiles()   #loads the world tiles from file
    player = game.Player()    #creates a new player object
    room = tile_exists(player.location_x, player.location_y) 
    print(room.intro_text())
    
    while player.is_alive() and not player.win:
        room = tile_exists(player.location_x, player.location_y) #the location
        
        room.modify_player(player) #modifys player location
        
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.win:
            available_actions = room.available_actions() #displays all the avaiable actions
            for action in available_actions:
                print(action)
            action_input = input('What are you going to do?: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
                
                



def tile_exists(x, y):
        """Returns the tile at the given coordinates or None if there is no tile.

        :param x: the x-coordinate in the worldspace
        :param y: the y-coordinate in the worldspace
        :return: the tile at the given coordinates or None if there is no tile
        """
        return _world.get((x, y))


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('game'), tile_name)(x, y)
if __name__ == "__main__":
    play()