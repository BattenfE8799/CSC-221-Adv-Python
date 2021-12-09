# CCS-221
# M2HW1
# Elizabeth Battenfield

import pandas as pd
import sys

def main(): 
    """main menu"""
    #put menu as main to lessen complication
    df = pd.read_csv('diamonds.csv', index_col=0)
    print('\n\nMenu')
    print("1. Display First Seven Rows")
    print("2. Display Last Seven Rows")
    print('3. Calculate Descriptive Statistics for "Carat"')
    print('4. Calculate Descriptive Statistics for "Cut","Color", and "Clarity"')
    print('5. Display Unique Category Values for "Cut","Color", and "Clarity"')
    print('6. Display Histogram of each Numerical Column')
    print('7. Exit Program')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        displayFirst(df)
    elif choice == 2:
        displayLast(df)
    elif choice == 3:
        calculateCarat(df)
    elif choice == 4:
        calculateCut(df)
    elif choice == 5:
        displayUnique(df)
    elif choice == 6:
        displayHistogram(df)
    elif choice == 7:
        exitProgram()
    else: #simple version of verification
        print("\nInvalid Entry. Enter Correct Value.\n")
        main() 


def displayFirst(df):
    """
    displays first seven rows
    """    
    print('\n', df.head(7))#simpler just to put the code as print
    main() #repeats menu
    
def displayLast(df):
    """ 
    displays Last seven rows
    """
    print('\n', df.tail(7))#simpler to just put code as print
    main()
def calculateCarat(df):
    """
    Calculate descriptive statistics for "carat"
    """
    print('\nCarat\n',df.carat.describe())#using print to make 'titles' for each one
    print('\nTable\n',df.table.describe())# instructions says to complete point e, which asks for more than carat
    print('\nprice\n',df.price.describe())
    print('\nx\n',df.x.describe())
    print('\ny\n',df.y.describe())
    print('\nz\n',df.z.describe())
    
    main()
def calculateCut(df):
    """
    Calculate descriptive statistics for "Cut". "color", "clarity"
    """
    print('\nCut\n',(df.cut).describe())#uses print to make 'titles' for each one to lessen confusion
    print('\nColor\n',(df.color).describe())
    print('\nClarity\n',(df.clarity).describe())
    main()
def displayUnique(df):
    """
    Display unique category values for "cut", 'color', and 'clarity'
    """
    print('\nCut\n',(df.cut).unique()) #took me awhile to find this, as book wasn't helpful
    print('\nColor\n',(df.color).unique())#the describe series unique method on the internet just replaces describe with unique on the commands
    print('\nClarity\n',(df.clarity).unique())
    main()    

def displayHistogram(df):
    """
    display histogram of each Numerical Column
    """
    %matplotlib
    print('\nHistograms\n') 
    #i have a weird error or something where when I run this it pops up the box,
    #but it says"Not responding" until I hit the red square stopping the current 
    #command. Then it shows the charts. Theres no issue if I just type the command in the console
    
    df.hist()#supposed to show all of the numerical columns histographs in same image
    main()
def exitProgram():
    print("Goodbye")
    sys.exit()#uses sys import to exit, because i still can't get it to work without importing sys
    
    
if __name__ == "__main__":
    main()