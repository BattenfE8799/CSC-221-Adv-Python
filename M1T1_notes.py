# CTS-285
# M1T1-Orientation/notes from class

# Elizabeth Battenfield
# 8/16/2021

"""
Orientation Introduction
"""
print()
print("Hello!\n")
print( "I'm Elizabeth Battenfield.\n\n")
print("This semester I have a full study load!\n\n")
print( "I am studying Advanced C++ and Advanced Python!\n\n")
print( "I am also studying:\n      Operating System Concenpts,\n      System Analysis and Design, and\n      Linux/Single User (aka Red Hat System Administration 1)\n\n")
print( "I am a single mother, I am currently not working as I am a full-time student.\n\n")
print( "I am planning on graduating this coming spring, and hope to get a good job using what I've learned here at FTCC.\n\n")
print( "My hobbies include listening to music, reading, playing video games, and watching youtube/twitch streamers.\n\n")
print( " I am also spending my time making my own personal projects using Python and C++.\n\n")
print( "My current long term project is a text-based Pokemon game.\n")
print("!!!!!")
#yes, i used the exact same as the C++ i had alread done. 
#done with what I learned 
print(""""Hello!\n
I'm Elizabeth Battenfield.\n\n
This semester I have a full study load!\n\n
      I am studying Advanced C++ and Advanced Python!\n\n
I am also studying:\n      Operating System Concenpts,\n      System Analysis and Design, and\n      Linux/Single User (aka Red Hat System Administration 1)\n\n
I am a single mother, I am currently not working as I am a full-time student.\n\n
I am planning on graduating this coming spring, and hope to get a good job using what I've learned here at FTCC.\n\n
My hobbies include listening to music, reading, playing video games, and watching youtube/twitch streamers.\n\n
I am also spending my time making my own personal projects using Python and C++.\n\n
My current long term project is a text-based Pokemon game.\n !!!!!!""")

#can use ''' to test things
"""
print()
print("Hello!\n")
print( "I'm Elizabeth Battenfield.\n\n")
print("This semester I have a full study load!\n\n")
print( "I am studying Advanced C++ and Advanced Python!\n\n")
print( "I am also studying:\n      Operating System Concenpts,\n      System Analysis and Design, and\n      Linux/Single User (aka Red Hat System Administration 1)\n\n")
print( "I am a single mother, I am currently not working as I am a full-time student.\n\n")
print( "I am planning on graduating this coming spring, and hope to get a good job using what I've learned here at FTCC.\n\n")
print( "My hobbies include listening to music, reading, playing video games, and watching youtube/twitch streamers.\n\n")
print( " I am also spending my time making my own personal projects using Python and C++.\n\n")
print( "My current long term project is a text-based Pokemon game.\n")
print("!!!!!")
"""
#list
myInfo = ["Name", "Language","Personal"]
#prints list
print(myInfo)
#prints the string in the list
print(myInfo[0])

#constants
PI_CONST = 3.14 #all caps says dont change, but python can still change it. BeCareful

#every object can be printed
myInfo #prints list
print(myInfo) #prints list
name = myInfo[0] #creates oject
name #prints with ' '
print(name) #prints with no ' '

#the idea of a list is not a list
#aka len(list) wont work on unless there is an object named list

#to find out the type
type(myInfo)
type(range(5))

#manual inpacting
#name, lang, personal gets myInfo
name, lang, personal = myInfo
print(name)
print(lang)
print(personal)
# = is not equals its gets
# x gets 2: x=2
# : is the slice command
myInfo[1:] #chops off the  first item
myInfo[:1] #chops off the last item
myInfo[1:2] #chops off the 1 and 2 items
del myInfo[2] #deletes the 2 in the list
myInfo

#comprehensions for list
list1 = [item for item in range(1,6)]
list1
type(range(1,6))
type(list1)
list2 = [item * 5 for item in range(1,6)]
list2
list3 = [item for item in range (1,12) if item % 2 ==0]
list3



#numpy crunches the data in an array
#used for 3d
#can you put an array into an array

