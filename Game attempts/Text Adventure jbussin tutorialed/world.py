
_world = {} 
starting_position = (0, 0)

def tile_exists(x,y):
    return _world.get((x,y))

def load_tiles():
     """Pareses a file that describes the world space into the _world object"""
     file = 'resources/map.txt' #hopefully this will allow custome file to be sent here per game
     with open(file, 'r') as f:     #opens the map.txt
         rows = f.readlines()                      #creates rows by reading line by line
     x_max = len(rows[0].split('\t'))              #creats max of x corrdinate, its the number of items in a row, split by the tabs
     for y in range(len(rows)):                    
         cols = rows[y].split('\t')                #creates y coordinates, same amount as x  
         for x in range(x_max):                    #for each tile
             tile_name = cols[x].replace('\n', '') #writes each tile name as what is in file
             if tile_name == 'StartingRoom':         #creates starting postion if tile is named starting room
                 global starting_position
                 starting_position = (x,y) 
             _world[(x, y)] = None if tile_name == '' else getattr(__import__('peg_game'), tile_name)(x, y)




 ##^^ goes through each line of the file and splits the line into cells. 
 #Using a double: for loop, is a common way of working with grids.
 #x and y keep track of cooridinates
 #when finding the starting room, that position is saved, because we will use it later
 #global variable will let up access the starting_position variable outside of this method
 #_world is a dicationary that maps a coordinate pair to a title. 
 #_world[(x,y)] creates the key(coordinate pair) of the dictionary. 
 #if tile is empty string we dont want to store a tile in its place, so None if tile_name == ''
 #creates tile if contains name
 
 #getattr method is build into python
 #lets reflect into the tile module and find the class whose name matches the tile_name.
 #(x,y) passes the coords to the constructor of the tile
 
 

