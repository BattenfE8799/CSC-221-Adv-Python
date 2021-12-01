

class Person:
    def __init__(self, firstName,lastName, email):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_email(self, email):
        self.__email = email
    
    def get_firstName(self):
        return self.__firstName
        
    def get_lastName(self):
        return self.__lastName
    
    def get_email(self):
        return self.__email




class Employee(Person):
    def __init__(self, firstName, lastName, email, position, salary, full_part_time):
        super().__init__(firstName, lastName, email)
        self.position = position
        self.salary = salary
        self.full_part_time = full_part_time
        
    def __str__(self):
        # return f'{firstName} {lastName} {email}'
        return '{firstName}{lastName}{email}{position}{salary}{full_part_time}'
    
    def set_email(self):
        self.__email = self.get_lastName() + "." + self.get_firstName() + "@company.com"

# class Employee(Person):
#     def __init__(self, firstName, lastName, email, position, salary, full_part_time):
#         super().__init__(firstName, lastName, email)
#         self.email = email
#         self.__position = position
#         self.__salary = salary
#         self.__full_part_time = full_part_time
    
#     def set_email(self):
#         self.email = self.get_lastName() + "." + self.get_firstName() + '@company.com'
        
    
    def set_position(self, position):
        self.__position = position

    def set_salary(self, salary):
        self.__salary = salary

    def set_full_part_time(self, full_part_time):
        self.__full_part_time = full_part_time
    
    
    def get_email(self):
        return self.email 
        
    def get_position(self):
        return self.__position
        
    def get_salary(self):
        return self.__salary
    
    def get_full_part_time(self):
        return self.__full_part_time      





