# CTS-221
# M1LAB1- Double a number
# Elizabeth Battenfield
# 8/18/2021
"""

"""
results = []#global

def main():
    """Main loop of program."""
    print("Welecome to Double a Number Program")
    repeat = True
    while repeat == True:
            userInput()
            repeat = repeatOrNot()
    print("\n",numbersListed())
    print("Bye")
            

def userInput():

    """Collects user number"""
    num = int(input("\n Enter a number: "))
    dbl = num * 2
    # dbl = doubleNum(num)
    results.append(dbl)
    print("\n",num, "doubled is:", dbl)
    print(results)
    

def repeatOrNot():
    """ """
    print("\n1. Enter another number")
    print("2. Exit")
    goAgain = int(input())
    if 1 == goAgain:
        return True
    else:
        return False


def numbersListed():
    """prints the listed results"""
    print("\n All Your Results:")
    print(results)
    
    itera = len(results)
    index_1 = 0
    # index_2 = 1
    
    for counts in range(itera):
        print(f'{results[index_1]}')
        index_1 += 1
        # index_2 += 2
        
    
    
# 'traditional magic to invoke main'    
if __name__ == "__main__":
    main()