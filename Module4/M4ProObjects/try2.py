#Employee subclass of Person class
from person import Person


class Employee(Person):
    def __init__(self, firstName, lastName, email, position, salary, full_part_time):
        super().__init__(firstName, lastName, email)
        self.position = position
        self.salary = salary
        self.full_part_time = full_part_time
        
    def __str__(self):
        #return f'{firstName} {lastName} {email}'
        return f'{self.get_firstName()} {self.get_lastName()} {self.get_email()} {self.get_position()} {self.get_salary()} {self.get_full_part_time()}'
    
    def set_email(self):
        """ Error Testing : it works either way
            # lName = self.get_lastName().lower()
            # fName = self.get_firstName().lower()
            # # lName = lName.lower()
            # # fName = fName.lower()
            # self.__email = lName + "." + fName + "@company.com"
        """
        self.__email = self.get_lastName().lower() + "." + self.get_firstName().lower() + "@company.com"

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary

    def set_full_part_time(self, full_part_time):
        self.full_part_time = full_part_time
    
    
    def get_email(self):
        return self.__email 
        
    def get_position(self):
        return self.position
        
    def get_salary(self):
        return self.salary
    
    def get_full_part_time(self):
        return self.full_part_time  


# firstName = 'tim'
# lastName = "smith"
# email = "smith@company.com"
# #employee1 = Employee(firstName,lastName,email)
# employee1 = Employee('Tim', 'Smith', 'email', 'crew', 10, 'full')
# print(employee1)
# Employee.set_email(employee1)






#print(employee1)

# class Person:
#     def __init__(self, firstName,lastName, email):
#         self.__firstName = firstName
#         self.__lastName = lastName
#         self.__email = email

#     def set_firstName(self, firstName):
#         self.__firstName = firstName

#     def set_lastName(self, lastName):
#         self.__lastName = lastName

#     def set_email(self, email):
#         self.__email = email
    
#     def get_firstName(self):
#         return self.__firstName
        
#     def get_lastName(self):
#         return self.__lastName
    
#     def get_email(self):
#         return self.__email
