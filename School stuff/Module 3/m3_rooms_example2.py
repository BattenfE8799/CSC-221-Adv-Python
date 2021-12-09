# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:04:03 2021

@author: norrisa8373
"""

# Pass 2 of the Room class with full exits

class Room:
    """class for holding room names, descriptions, exits"""
        
    def __init__ (self, name, desc):
        self.name = name
        self.desc = desc
        # four exits, each points to another Room object
        self.north = None
        self.south = None
        self.east  = None
        self.west  = None
    
    def __str__ (self):
        roomText = "Room: " + self.name + "\n"
        roomText +="Description: " + self.desc
        roomText +="Exits: "
        if self.north != None:
            roomText +="N: " + self.north.name
        if self.south != None:
            roomText +="S: " + self.south.name
        if self.east != None:
            roomText +="E: " + self.east.name
        if self.west != None:
            roomText +="W: " + self.west.name
        return roomText
    
def main():
    """ test out the Room object."""
    rooms = []
    
    kitchen = Room("Kitchen", "There is a toaster here.")
    livingRoom = Room("Living Room", "The TV is off.")
    bedRoom    = Room("Bedroom", "Clothes are scattered.")
    
    # add the rooms to the master list
    rooms.append(kitchen)
    rooms.append(livingRoom)
    rooms.append(bedRoom)
    
    # next, link the exits to actual rooms
    kitchen.south = livingRoom
    livingRoom.north = kitchen
    
    livingRoom.east = bedRoom
    bedRoom.west = livingRoom
    
    currentRoom = livingRoom
    
    # now step through the rooms
    print(currentRoom)
    currentRoom = currentRoom.north
    
    print(currentRoom)
    currentRoom = currentRoom.south
    
    print(currentRoom)
    currentRoom = currentRoom.east
    
    print(currentRoom)
    
    
    
main()