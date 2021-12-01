"""
CSC-221
M4Pro Objects
Elizabeth Battenfield
11/15/2021
"""
from person import Person
from person import Employee
import sys
# function defenition module

def menu(): #define menu function
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
    
def enterInfo():
    howMany = int(input("How many employees' information do you want to enter? "))
    alist=[]
    with open("employees.txt", "w") as f:
        for item in alist:
            f.write("%s\n" % item)
            
    alist.append(f'{"First Name":<10s}{" ":4}{"Last Name":<10s}{" ":4}{"Email(company email)":<10s}{" ":4}{"Position":<10s}{" ":4}{"Full/Part time":<10s}{" ":4}{"Salary":<10s}')
    for x in range(howMany):
        fName = input("First Name: ")
        lName = input("Last Name: ")
        position = input("Job Position: ")
        time = input("Full/Part time: ")
        salary = input("Salary: $")
        email = 'email'
        employee = Employee(fName,lName,email,position,salary,time)
        email = Employee.set_email(employee)
        alist.append(f'{fName:<10s}{" ":4}{lName:<10s}{" ":4}{email:<10s}{" ":4}{position:<10s}{" ":4}{time:<10s}{" ":4}{salary:<10s}')
    
    with open("employees.txt", "w") as f:
        for item in alist:
            f.write("%s\n" % item)
            
    with open("employees.txt", "r") as f:
        for item in f:
            print(item)
            
    return

def readInfo():
    with open("employees.txt", "r") as f:
        for item in f:
            print(item)
    return

def leave():
    print("Goodbye!")
    sys.exit()

menu()

