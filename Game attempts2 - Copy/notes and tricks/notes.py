# from dataclasses import dataclass
# # # # -*- coding: utf-8 -*-
# # # """
# # # Created on Fri Jul 30 16:21:01 2021

# # # @author: Margaret
# # # """
# # # # desk is variable and has program ask user "What is the name of desk"
# # # desk = input("What is the name of the desk?  ")

# # # # has program tell what the name of the desk.
# # # print(desk)



# # import json #imports json objects and ability to translate
# # from pprint import pprint #shows how it was in string
# # """
# # JSON data
# # """

# # data ="""{
# # "company":"Amazon",
# # "Market":1.59,
# # "Country":"USA",
# # "exits":[
# # {"East":"Bedroom"},
# # {"West":"Bathroom"},
# # {"South":"Kitchen"}]}
# # """
# # data1 = """
# # [
# #  {
# #   "company":"Audible"
# #   },
# #  {
# #   "company":"Whole Foods"
# #   },
# #  {
# #   "company":"Amazon go"
# #   }
# #  ]
# # """

# #converting dictionary to Json
# #also used for writing to json file
# super_heros = {
#     "Justice_league":[
#         "Superman",
#         "Batman",
#         "Wonder Woman",
#         "Flash"
#     ],
#     "Avengers": [
#         "Captain America",
#         "Iron Man",
#         "Thor",
#         "Hulk",
#         "Black Widow"
#         ]
# }


# # {
# # "Name":"Bedroom",
# # "Description": "Its your bedroom.",
# # {"west": "Hall", "south": "Bathroom"}
# #  }
        
# import json
# json_file = 'amazon.json'


# #     json_data = json.loads(data)
# #     pprint(type(json_data))
# #     pprint(json_data)
# #     print(json_data['Market']) #pprint would show quotations
# #     print(json_data['company'])
    
# #     json_data1 = json.loads(data1)
# #     pprint(type(json_data1))
# #     print(json_data1)
    
# # #converting dictionary to json
# #     #super_heros_str = json.dumps(super_heros)
# #     super_heros_str = json.dumps(super.heros, indent=4)
# #     print(type(super_heros_str))
# #     print(super_heros_str)

# #to read json file into python dictionary
# #json.load json file to python object
# #json.loads json string to python object 
#     # with open(json_file) as fh:
#     #     json_dat a= json.load(fh)
#     #     print(type(json_data))
#     #     print(json_data)
    
# #write to json file

# #serialization(encoding) and deserialization(decoding)
# """
# serialization is convertubg python object into json string
# deserialization is from json to python objects
# """
# @dataclass
# class Person:
#     name: str
#     age: int
    
# john = Person("John", 40)
# """would look like: (json)
# {"name":"John",
#  "age":40}
# """
# # #manually serialize
# # jsonfied_john = f'(("john.name"), "age": (john.age)))'
# # print(jsonfied_john)

# #encoding funcion
# #sould return a json encodable verson of the object or raise typeerror
# def encoder_person(person):
#     if isinstance(person, Person):
#         return {'name': person.name, 'age': person.age}
#     raise TypeError(f'Object (person) is not of type Person.')

# class PersonEncoder(json.JSONEncoder):
#     """ encodes/serializes json"""
#     def default(self, o):
#         if isinstance(o, Person):
#             return {'name': o.name, 'age': o.age}
#         return super().default(o)
    

# if __name__ == '__main__':
#     # with open(json_file, 'w') as fh:
#     #     json.dump(super_heros, fh)
        
#     # with open(json_file, 'r', indent =4) as fh:
#     #     json.load()
#     #manual
#     jsonfied_john = f'"name": {"john.name"}, "age": {john.age}'
#     print(jsonfied_john)
#     #function
#     jsonfied_john = json.dumps(john, default=encoder_person)
#     print()
#     print(jsonfied_john)
#     #class
#     jsonfied_john = json.dumps(john, cls=PersonEncoder, indent=4)
#     print()
#     print(jsonfied_john)
#     #create an object of encoder class
#     encoded_person = PersonEncoder().encode(john)
#     print()
#     print(encoded_person)







































