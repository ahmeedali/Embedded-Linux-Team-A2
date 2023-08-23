#!/usr/bin/python3

import webbrowser

#Dictionary containing favorite websites url
favorites = {"Github"   : "https://github.com/",
             "Linkedin" : "https://www.linkedin.com/",
             "Youtube"  : "https://www.youtube.com/",
             "Facebook" : "https://www.facebook.com/",
             "Whatsapp" : "https://web.whatsapp.com/",
             "Gmail"    : "https://mail.google.com/mail/u/0/#inbox",
             }

#This function take one argument: (website address) and open it as new tab in Firefox
def Firefox(url):
    webbrowser.get('firefox').open_new_tab(url)

#This function print out favorite websites
def show_favorites():
    for key in favorites:
        print(key, ":   ", favorites[key])

#This function ask the user to select the favorite website to open by typing the name
#in case of entering an input not in the list it will ask again till having a valid input
def select_fav() -> str:
    key = input("Choose website to open: ")
    while(key.capitalize() not in favorites):
        print("Invalid input")
        key = input("Choose website to open: ")
    return favorites[key.capitalize()]

def test_function():
    show_favorites()
    f = select_fav()
    print(f)
    Firefox(f)

if __name__ == "__main__":
    test_function()