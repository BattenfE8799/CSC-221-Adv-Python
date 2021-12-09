# CSC 221
# M3T3 Linked Lists Examples
# name
# date

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
    
    
    # link the nodes into a list
    # example:
    #room1.next = room2

    

    
    
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
    
# run program
main()
