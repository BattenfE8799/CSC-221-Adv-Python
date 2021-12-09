# script that reads a speech from a file, then displays statistics about it. 
# Date
# CSC221 M2HW – FileExceptions
# Elizabeth Battenfield

import sys
import re



def main(): 
    """main menu"""
    file = open('stateoftheunion.txt', 'r') #placing here so i don't have to type this each time, i can just send it to each method and they have it
    #put menu as main to lessen complication
    print('\n\nMenu')
    print("1. Display Entire Speech")
    print("2. Display Total Word Count")
    print('3. Display Total Character Count')
    print('4. Display Average Word Length')
    print('5. Display Top Ten Longest Words')
    print('6. Exit Program')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        displaySpeech(file)
    elif choice == 2:
        displayWordCount(file)
    elif choice == 3:
        displayTotalChar(file)
    elif choice == 4:
        displayAverage(file)
    elif choice == 5:
        displayTopTen(file)
    elif choice == 6:
        exitProgram()
    else: #simple version of verification
        print("\nInvalid Entry. Enter Correct Value.\n")
        main()


def displaySpeech(file):
    """
    reads the txt file and displays the speech on screen
    """    
    speech = file.read() #reads the file 
    print(speech)
    file.close() #remembered to close the file
    main() #repeats menu
    
def displayWordCount(file):
    """ 
    reads the text file and displays total word count
    """
    data = file.read()
    words = data.split()
    file.close()
    print("\nTotal Number of Words: ", len(words)) #uses len to get total word count
    main()
def displayTotalChar(file):
    """
    reads the text file and displays total character count
    """
    data = file.read()
    characters = 0 
    for line in data:
        line = line.strip("\n") #removes the spaces between letters  
        words = line.split() #splits the string into a list
        characters += len(words) #counts the length of the list, with no spaces this is the number of characters in the speech
    file.close()
    print("\nTotal Number of Characters: ",characters)
    
    main()
def displayAverage(file):
    """
     reads the text file and displays average word length
    """
    data = file.read()
    words = data.split()
    average = sum(len(word) for word in words) / len(words)#calulates the average word length by taking length of each word and adding them together and then dividing that number by the number of words
    averageRounded = round(average, 2) #wanted it to look neater so rounded it using the round function
    print("\nAverage Word Length: ", averageRounded)
    main()
def displayTopTen(file):
    """
    reads the text file and displays the top ten longest words
    """
    data = file.read()
    # punc = '''`!()-[]{};:'"\,<>./?@#%^&*_~''' #has a punctuation issue with longest words, this lists all the symbols to removes them
    # for ele in data:
    #     if ele in punc:
    #         data = data.replace(ele," ")
    
    
    x = re.split('. |!|,|;|-|\n',data) 
    words = x
    sep_words = list(set(words)) #set checks if there are duplicated
    words = sorted(sep_words,key=len) 



    x=10
    for _ in range(10):
        x += 1
        print(words[-x])
    print()
    
    file.close()
            
    main()

def exitProgram():
    """ 
    exits program
    """
    print("Goodbye")
    sys.exit()#uses sys import to exit, because i still can't get it to work without importing sys
    

if __name__ == "__main__":
    main()