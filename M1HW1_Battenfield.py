# -*- coding: utf-8 -*-
"""
# CTS-221
# M1LAB1- Double a number
# Elizabeth Battenfield
# 8/22/2021
"""

def main():
    """Calculator program"""
    print()
    print("+=*Calculator*=+")
    print()
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    choice = int(input("Your Choice: "))
    
    if choice == 1:
        addNum()
    elif choice == 2:
        minNum()
    elif choice == 3:
        divideNum()
    elif choice == 4:
        multiplyNum()
    elif choice == 5:
        print()
        print("Bye")
        return
    else:
        print()
        print("!!!Error!!!")
        print("Invalid choice.")
        main()
    
def addNum():
    """addition calculator"""
    print()
    print("Add")
    x = int(input("Enter a number:"))
    y = int(input("Enter a number:"))
    z = x + y
    print(x, " + ", y, " = ", z)
    repeatOrNot()    
    
def repeatOrNot():
    """Asks user whether or not to repeat program"""
    print("\n1.Again")
    print("2.Menu")
    goAgain = int(input("Your Choice:"))
    if goAgain == 1:
        addNum()
    elif 2 == goAgain:
        main()
    else:
        print("Invalid Choice, try again.")
        repeatOrNot()      

def minNum():
    """addition calculator"""
    print()
    print("Subtract")
    x = int(input("Enter a number:"))
    y = int(input("Enter a number:"))
    z = x - y
    print(x, " - ", y, " = ", z)
    repeatOrNot2()    
    
def repeatOrNot2():
    """Asks user whether or not to repeat program"""
    print("\n1.Again")
    print("2.Menu")
    goAgain = int(input("Your Choice:"))
    if goAgain == 1:
        minNum()
    elif 2 == goAgain:
        main()
    else:
        print("Invalid Choice, try again.")
        repeatOrNot2()   
    
    
def divideNum():
    """addition calculator"""
    print()
    print("Divide")
    x = int(input("Enter a number:"))
    y = int(input("Enter a number:"))
    z = int(x / y)
    print(x, " / ", y, " = ", z)
    repeatOrNot3()    
    
def repeatOrNot3():
    """Asks user whether or not to repeat program"""
    print("\n1.Again")
    print("2.Menu")
    goAgain = int(input("Your Choice:"))
    if goAgain == 1:
        divideNum()
    elif 2 == goAgain:
        main()
    else:
        print("Invalid Choice, try again.")
        repeatOrNot3()       
    
def multiplyNum():
    """addition calculator"""
    print()
    print("Multiply")
    x = int(input("Enter a number:"))
    y = int(input("Enter a number:"))
    z = x * y
    print(x, " * ", y, " = ", z)
    repeatOrNot4()    
    
def repeatOrNot4():
    """Asks user whether or not to repeat program"""
    print("\n1.Again")
    print("2.Menu")
    goAgain = int(input("Your Choice:"))
    if goAgain == 1:
        multiplyNum()
    elif 2 == goAgain:
        main()
    else:
        print("Invalid Choice, try again.")
        repeatOrNot4()       
    
    
if __name__ == "__main__":
    main()