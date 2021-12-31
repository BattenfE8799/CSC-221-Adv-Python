from dataclasses import dataclass, astuple, asdict, field
import inspect
from pprint import pprint
"""
v1: read and write to a file works. 
- can make instances with lines read from file.
- checks to see if item exists before appending it to file.
- appends to end of file
-- adds newline so its not all on one line
--TODO: 
    -Adjust checking if exists so it has to be exact. So health potion doesnt equal potion.
    --use word boundaries to mark names specficially
v2: fixed issue with last character disapearing, and fixed exact lookup
    
"""
@dataclass(frozen=True, order=True) #immutable with frozen =true
class Items:
    name: str
    description: str
    value: int = 0
    
    def __str__(self):
        return f'{self.name}: {self.description} Value: {self.value}'
    
def main():
    listing = []
    listing = item_setup()
    if len(listing)==0:
        print("\nThere are no items in the game.\n")
    else:
        print("\nItems in game: \n")
        for item in listing:
            print(item)
        
def item_setup_adding_Items():
    listing = []
    numItems = int(input("How many items will you add?\n Do not use ';': "))
    for x in range(numItems):  
        with open('items.txt', 'r') as txt:
            itemname = input("Item Name: ")
            itemDescription = input("Description: ")
            itemValue = input("Item Value: ")
            item = f'\b{itemname}\b; {itemDescription}; {itemValue}'
            newName = f'\b{itemname}\b'
                
            #search through text file
            readfile = txt.read()
            print(newName)
            if newName in readfile:
                print("\n It's already there.\n")
                
            else:
                txt.close()
                with open('items.txt', 'a') as txt:
                    txt.write(item)
                    txt.write("\n")
                    txt.close()

def item_setup():
    item_setup_adding_Items()
    listing = []
    with open('items.txt', 'r') as txt:
        for line in txt:
            name, description, value = line.split(';')
            name = name.replace("\b","")
            listing.append(Items(name, description, value))
    return listing
        

    
        
    
    
    
if __name__ == '__main__':
    main()
    