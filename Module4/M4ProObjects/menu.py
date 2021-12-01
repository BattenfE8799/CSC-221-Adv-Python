"""
CSC-221
M4Pro Objects
Elizabeth Battenfield
11/15/2021
"""
from person import Person
from try2 import Employee
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
            
    alist.append(f'{"First Name":<10s}{" ":4}{"Last Name":<10s}{" ":4}{"Email(company email)":<25s}{" ":8}{"Position":<10s}{" ":4}{"Full/Part time":<10s}{" ":4}{"Salary":<10s}')
    for x in range(howMany):
        fName = input("First Name: ")
        lName = input("Last Name: ")
        position = input("Job Position: ")
        time = input("Full/Part time: ")
        salary = input("Salary: $")
        employee1 = Employee(fName,lName,'email',position,salary,time)
        Employee.set_email(employee1)
        print(employee1)
        email = Employee.get_email(employee1)
        print(email)
        alist.append(f'{fName:<10s}{" ":4}{lName:<10s}{" ":4}{email:<25s}{" ":8}{position:<10s}{" ":4}{time:<10s}{" ":4}{salary:<10s}')
        print(len(alist))
    # \t makes a tab
    with open("employees.txt", "w") as f:
        for item in alist:
            f.write(item+"\n") 
            
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

