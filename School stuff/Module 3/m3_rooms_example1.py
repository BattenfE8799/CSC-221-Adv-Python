# Practice code for TextAdv Project
# (Will be an assignment)

# first pass - just a list?

roomNames = ['1', '2', '3']
roomDescs = ['kitchen', 'living room', 'bedroom']

"""
for name in roomNames:
    print (name)
    
for desc in roomDescs:
    print (desc)
    
# take 2 - dictionary
rooms = [ {"name":"1", "desc": "kitchen"},
          {"name":"2", "desc": "living room"},
          {"name":"3", "desc": "bedroom"}]

for room in rooms:
    print("room name:",room["name"])
    print("room description:",room["desc"])
"""
# take 3 - class
class Room:
    def __init__ (self, name, desc):
        self.name = name
        self.desc = desc
    
    def __str__ (self):
        roomText = "Room: " + self.name + "\n"
        roomText +="Description: " + self.desc
        return roomText

rooms = [Room("1", "kitchen"),
         Room("2,","living room"),
         Room("3","bedroom")]

for room in rooms:
    print(room)
        

