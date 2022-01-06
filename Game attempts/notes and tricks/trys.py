# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 16:29:30 2021

@author: Momma Brat
"""
from gameSetup import Room


# """ sets up the game"""
bedroom = Room('Bedroom',"Its you and your spouse's bedroom.",[], {"west": "Living Room", "south": "Bathroom"})
livingroom= Room("Living Room","Its the livingroom, everyone spends alot of time here.\n.",[], {"east": "Bedroom"})
bathroom = Room("Bathroom", "Its the bathroom!", [], {"north": "Bedroom"})

rooms = {"bedroom" : Room('Bedroom',"Its you and your spouse's bedroom.",[], {"west": "Living Room", "south": "Bathroom"}),
"livingroom": Room("Living Room","Its the livingroom, everyone spends alot of time here.\n.",[], {"east": "Bedroom"}),
"bathroom": Room("Bathroom", "Its the bathroom!", [], {"north": "Bedroom"})}

import json

# def write_json(data, filename='testing.json'):
#     with open (filename, "w") as f:
#         json.dump(data, f, indent =4)
        
# with open ("testing.json") as json_file:
#     data = json.load(json_file)
#     temp = data["rooms"]
#     y = rooms
#     temp.append(y)
    
# write_json(data)
data = [{"Game Title": 
"Game title goes here"},
{ "Intro": 
"Intro for game goes here"},
{"Ending": 
"Ending of game goes here"}]
    
with open ("testing.json", 'w') as f:
    json.dump(data, f)
    data = json.loads(data)
    print(data)
    
# with open ("testing.json") as json_file:
#     data = json.load(json_file)
#     temp = data["rooms"]
#     y = rooms
#     temp.append(y)

    

    