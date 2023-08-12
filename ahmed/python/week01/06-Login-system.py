#!/usr/bin/python3
# Creating a Dictionary 
# with string Keys
LoginData  ={ 'ahmed' : 111,'ali':222, 'amr': 333} 

User = input ("please enter your name : ")
if User in LoginData :
    print("Welcome "+ User)
    password = int (input ("please enter your password: "))
    if password == LoginData[User] :
        print("creat .. have a nice day "+ User)
    else :
        print ("incorrect")
else :
    print ("invalid input user")
    