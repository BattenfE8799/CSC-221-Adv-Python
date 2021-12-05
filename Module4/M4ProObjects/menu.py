"""
CSC-221
M4Pro Objects
Elizabeth Battenfield
11/15/2021
"""
from person import Person
from employee import Employee
import sys
# function defenition module

def main(): #define menu function
    #display menu choices
    wrong = True
    while wrong == True:
        print("1) Enter Employee Info\n2) Read Employee Info\n3) Exit")
        choice = int(input("Your choice: "))
        
        if choice == 1:
            enterInfo()
        elif choice == 2:
            readInfo()
        elif choice == 3:
            leave()
        else:
            print("Invlid choice please try again.")
            wrong = True
#have them enter the employees information
def enterInfo():
    howMany = int(input("How many employees' information do you want to enter? "))
    alist=[]
     #add the header to the file      
    alist.append(f'\n{"First Name":<10s}{" ":4}{"Last Name":<10s}{" ":4}{"Email(company email)":<25s}{" ":8}{"Position":<10s}{" ":4}{"Full/Part time":<15s}{" ":4}{"Salary":<10s}')
    #loops the information requests and writing to a list for as many times as the user wants to enter employees
    for x in range(howMany):
        fName = input("First Name: ")
        lName = input("Last Name: ")
        position = input("Job Position: ")
        time = input("Full/Part time: ")
        salary = input("Salary: $")
        print()
        employee1 = Employee(fName,lName,'email',position,salary,time)
        Employee.set_email(employee1)
        email = Employee.get_email(employee1)
        alist.append(f'{fName:<10s}{" ":4}{lName:<10s}{" ":4}{email:<25s}{" ":8}{position:<10s}{" ":4}{time:<15s}{" ":4}{salary:<10s}')
    # \t makes a tab
    with open("employees.txt", "w") as f:
        for item in alist:
            f.write(item+"\n") 
            
    return

def readInfo():
    #if the file is not there, return with an exception message saying there is no file with that name
    #read the file if it is there
    try:
        with open("employees.txt", "r") as f:
            for item in f:
                print()
                print(item)
        return
    except:
        print("\nThere's not an employees.txt file in this folder.\n\nPlease enter employee information from the menu to create the file.\n\n")
        
        
# end program if requested
def leave():
    print("Goodbye!")
    sys.exit()

if __name__ == "__main__":                
    main()