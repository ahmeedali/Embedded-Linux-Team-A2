#!/usr/bin/python3

import webbrowser
import pyautogui
from time import sleep

# Pause time interval between each pyautogui command
pyautogui.PAUSE = 1

Gmail = "https://mail.google.com/mail/u/0/#inbox"

# Trying to open Gmail in a new tab in Firefox
try:
    webbrowser.get('Firefox').open_new_tab(Gmail)
except Exception as e:
    # Print the exception message
    print(f"An exception occurred: {str(e)}")
else:
    print("SUCCESS")

sleep(3)

# Check if gmail has opened
gmail_entry = pyautogui.locateOnScreen("gmail_opened.png", confidence=0.8, minSearchTime=8)
if gmail_entry:
    
    # Check more icon inside the inbox in gmail
    more_x, more_y = pyautogui.locateCenterOnScreen("gmail_more.png", confidence=0.8, minSearchTime=4)
    if(more_x or more_y):
        # Open more icon inside the inbox in gmail
        pyautogui.moveTo(more_x, more_y)
        pyautogui.click()

        # Check mark as read icon has opened
        mark_x, mark_y = pyautogui.locateCenterOnScreen("gmail_mark_as_read.png", confidence=0.8, minSearchTime=4)
        if(mark_x or mark_y):
            # Select mark as read option
            pyautogui.moveTo(mark_x, mark_y)
            pyautogui.click()   
        else:
            print('Error: could not locate mark as read option')
    
    else:
        print('Error: could not locate more icon')


else:
    print('Error: gmail page could not open successfully')


