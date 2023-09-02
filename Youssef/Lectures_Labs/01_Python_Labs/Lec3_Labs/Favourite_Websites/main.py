""" 
   Autor      :     Youssef Adel Youssef
Description   :     Make your module that contain favourite websites and have function 
                    called Firefox take url and open website 
"""

import favourites

def Print_Menu():
    print()
    print("********** Menu **********")
    print("0. Exit")
    print("1. Open Facebook")
    print("2. Open Twitter")
    print("3. Open Linkedin")
    

def Get_User_Choice():
    choice = input("Enter your choice: ")
    return int(choice)

def Handle_Choice(choice):
    if   choice == 0:
        return False
    elif choice == 1:
        favourites.Firefox("https://www.facebook.com/")
    elif choice == 2:
        favourites.Firefox("https://twitter.com/?lang=en")
    elif choice == 3:
        favourites.Firefox("https://www.linkedin.com/")
    else:
        print("Invalid choice. Please try again.")

    return True


while True:
    Print_Menu()
    user_choice = Get_User_Choice()
    if not Handle_Choice(user_choice):
        break