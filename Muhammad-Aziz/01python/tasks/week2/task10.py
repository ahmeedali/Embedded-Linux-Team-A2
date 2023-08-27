#! /usr/bin/python3
#Using “Pyautogui” to open Emails and change Emails from unread to read

import webbrowser, time, pyautogui

webbrowser.open("https://www.gmail.com")
time.sleep(10)
pyautogui.moveTo(2292,205)
pyautogui.click()
time.sleep(5)
print(pyautogui.position())
time.sleep(3)
pyautogui.moveTo(2571,205)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(2292,205)
pyautogui.click()
