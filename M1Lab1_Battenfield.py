# CTS-221
# M1LAB1- Double a number
# Elizabeth Battenfield
# 8/18/2021
"""

"""
results = [] #global

def main():
    """Main loop of program."""
    print()
    print("Welecome to Double a Number Program")
    repeat = 1
    while repeat == 1:
            userInput()
            repeat = repeatOrNot()
    print()
    numbersListed()
    print()
    print("Bye")
    
def userInput():
    """Collects user number"""
    num = int(input("\n Enter a number: "))
    dbl = doubleNum(num)
    results.append(dbl)
    print("\n",num, "doubled is:", dbl)
    return()    

def repeatOrNot():
    """Asks user whether or not to repeat porgraom"""
    print("\n1. Enter Another Number ")
    print("2. Show all results")
    print("3. Exit")
    goAgain = int(input("Your Choice: "))
    if goAgain == 1:
        return 1
    elif 2 == goAgain:
        numbersListed()
        repeatOrNot()
    elif 3 == goAgain:
        return 3
    else:
        print("Invalid Choice, try again.")
        repeatOrNot()    
    
    
def doubleNum(num):
    """input: one number. output: the number * 2."""
    result = num * 2
    return result

def numbersListed():
    """prints the listed resutls"""
    print("\n All your results:")
    for num in results:
        print(num)

# 'traditional magic to invoke main'    
if __name__ == "__main__":
    main()
