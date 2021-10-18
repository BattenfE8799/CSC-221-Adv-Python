# CTS-285
# M2T2
# Elizabeth Battenfield

import os
import json

def nineThree():
    """
    9.3 sample code and self check code
    """
    print("\n9.3.1 sample code\n")
    with open('accounts.txt', mode='w') as accounts:
        print('100 Jones 24.98', file=accounts) #writes to a file and prints. automatically outputs a \n
        accounts.write('200 Doe 345.67\n') #used for behind the scenes input. 
        accounts.write('300 White 0.00\n')
        accounts.write('400 Stone -42.16\n')
        accounts.write('500 Rich 224.63\n')
    
    print("\n9.3.1 Self check code\n")
    with open('grades.txt', mode='w') as grades:
        print('1 Red A', file=grades)
        print('2 Green B', file=grades)
        print('3 White A', file=grades)
        
    print("\n9.3.2 sample code\n")
    with open('accounts.txt', mode='r') as accounts:
        print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
        for record in accounts:
            account, name, balance = record.split()
            print(f'{account:<10}{name:<10}{balance:>10}')
                        
    
    print("\n9.3.2 self check code\n")
    with open('grades.txt', mode='r') as grades:
        print(f'{"ID":<4}{"Name":<7}{"Grade"}')
        for record in grades:
            student_id, name, grade = record.split()
            print(f'{student_id:<4}{name:<7}{grade}')    
    
    
def nineFour():
    """
    9.4 sample code and self check code
    """
    print("\n9.2.1 sample code\n")
    accounts = open('accounts.txt', 'r')
    temp_file = open('temp_file.txt','w')
    with accounts, temp_file:
        for record in accounts:
            account, name, balance = record.split()
            if account != '300':
                temp_file.write(record)
            else:
                new_record = ' '.join([account, 'Williams', balance])
                temp_file.write(new_record + '\n')
    os.remove('accounts.txt')
    os.rename('temp_file.txt','accounts.txt')
    
    print("\n9.2.1 self check code\n")    
    accounts = open('accounts.txt', 'r')
    temp_file = open('temp_file.txt','w')
    with accounts, temp_file:
        for record in accounts:
            account, name, balance = record.split()
            if account != '200':
                temp_file.write(record)
            else:
                new_record = ' '.join([account, 'Smith', balance])
                temp_file.write(new_record + '\n')
    os.remove('accounts.txt')
    os.rename('temp_file.txt','accounts.txt')    
    

def nineFive():
    """
    9.5 sample code and self check code
    """
    print("\n9.3 sample code \n")
    accounts_dict = {'accounts': [{'account': 100, 'name': 'Jones','balance': 24.98},{'account': 200,'name':'Doe','balance': 345.67}]}
    with open('accounts.json','w') as accounts:
        json.dump(accounts_dict, accounts)

    with open('accounts.json','r') as accounts:
        accounts_json = json.load(accounts)
    print(accounts_json, '\n')
    print(accounts_json['accounts'],'\n')
    print(accounts_json['accounts'][0],'\n')
    print(accounts_json['accounts'][1],'\n')
    
    with open('accounts.json','r') as accounts:
        print(json.dumps(json.load(accounts),indent=4))
    
    print("\n9.5 self check code \n")
    grades_dict = {'gradebook':[{'student_id': 1, 'name':'Red','grade':'A'},{'student_id': 2, 'name': 'Green', 'grade': 'B'},{'student_id': 3, 'name': 'White', 'grade': 'A'}]}
    
    with open('grades.json','w') as grades:
        json.dump(grades_dict, grades)
    
    with open('grades.json','r') as grades:
        print(json.dumps(json.load(grades),indent=4))
    
    

def main():
    nineThree()
    nineFour()
    nineFive()

if __name__ == "__main__":
    main()