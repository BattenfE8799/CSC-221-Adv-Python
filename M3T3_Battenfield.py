# CSC 221
# M3T3 Linked Lists Examples
# Elizabeth Battenfield

# Purpose of the assignment:
# Add your five rooms below
# Using the existing code, make sure you can walk from room 1 to room 5
# Then add code to walk back (using the 'prev' value) from room 5 to room 1

class Node:
    """Nodes are used to make linked lists. They contain a value, 
    and optionally, a "pointer" to the next node."""
    
    def __init__ (self):
        self.value = None
        self.next = None
        self.prev = None
        
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__ (self):
        """Just print the value for now"""
        return "Node: value = " + str(self.value)

    
def main():
    """ Create a linked list of Five nodes, each containing
    one of your room names as the value """
    # example:
    #room1 = Node("bedroom")
    room1 = Node("bedroom")
    room2 = Node("living room")
    room3 = Node("front yard")
    room4 = Node("kitchen")
    room5 = Node("back yard")
    
    # link the nodes into a list
    # example:
    #room1.next = room2 
    
    room1.next = room2
    room2.next = room4
    room4.next = room5
    room5.next = room3
    
    room3.prev = room5
    room5.prev = room4
    room4.prev = room2
    room2.prev = room1
    
    
    

    
    
    """ Next, traverse the linked list, printing each name. """
    location = room1
    for i in range(5):
        print(location)
        print("moving to next room...")
        if location.next != None: 
            location = location.next 
        else:
            print("No next room to go to!")
            
    print("-" * 20)  # separator
    """ Now do it again backwards. """
    for i in range(5):
        pass
        # your code to walk backwards goes here
        print(location)
        print("moving to the previous room..")
        if location.prev != None:
            location = location.prev
        else:
            print("No next room to go.")
    
# run program
main()
