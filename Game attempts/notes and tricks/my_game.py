# -*- coding: utf-8 -*-
"""
My game for game engine
v1- useing json to load data
 --setting up dataclasses for baseitems and containers
 
"""
from dataclasses import dataclass #enables use of dataclass
import json                       #import json to use json objects and files
from gameSetup import BaseItem, Container, Player, Game, Room, ItemEncoder

def Load():
    save_file = 'save.json'
    items = []
    rooms = {}
    player = Player
    
    with open (save_file, 'r') as sf:
        save = json.loads(sf)
        print(save)


def Save(rooms, items, player, filename="save.json"):
    print(rooms, items, player)
    with open (filename, 'w') as f:
        data = json.load(filename)
        temp = data["rooms"]
        y = rooms
        temp.append(y)
        json(data, f, indent = 4)
    

# def write_json(data, filename="01_names.json"):
#     with open (filename, 'w') as f:
#         json.dump(data, f, indent = 4)
        
# with open ("01_names.json") as json_file:
#     data = json.load(json_file)
#     temp = data["names"]
#     y = {"firstname": "joe", "age" : 40}
#     temp.append(y)
    
# write_json(data)

if __name__ == '__main__':
    gameSetup.main()
    
    
    
    # shelter_key = BaseItem("key", "Its the key that unlocks the shelter.")
    # bedroom = Room('Bedroom',"Its you and your spouse's bedroom.", [], {"west": "Hall", "south": "Bathroom"})
    # player = Game.here
    # rooms = [bedroom]
    # items = [shelter_key]
    # #pass item into  saveitems to turn into json data
    # Save(rooms, items, player)
    # Load()
    # list, tuple = array
    #dict =object
    #str = string
    #int, float = number
    #True and False = true and false
    #none = null
    
