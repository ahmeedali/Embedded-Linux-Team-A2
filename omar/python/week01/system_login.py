#!/usr/bin/python3

systemData = {'Ahmed':  1394,
              'Ali':    6098,
              'Amr':    9345}

#Todo:  capitalize first letter of the input
#       Add validation that the entered username is in the list
userName = input("Please enter User Name: ")
print(systemData[userName])

password = int(input("Please enter your password: "))

if systemData[userName] != password:
    print("Incorrect entry")
else:
    print("Welcome", userName)