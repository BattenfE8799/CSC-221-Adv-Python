#Employee subclass of Person class
from person import Person


class Employee(Person):
    def __init__(self, firstName, lastName, email):
        super().__init__(firstName, lastName, email)
        # self.position = position
        # self.salary = salary
        # self.full_part_time = full_part_time
        
    def __str__(self):
        return f'{firstName} {lastName} {email}'
        #return '{firstName}{lastName}{email}{position}{salary}{full_part_time}'
    
    def set_email(self):
        Person.__email = Person.__lastName + "." + Person.__firstName + "@company.com"



firstName = 'tim'
lastName = "smith"
email = "smith@company.com"
employee1 = Employee(firstName,lastName,email)
print(employee1)
Employee.set_email(employee1)


print(employee1)

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
