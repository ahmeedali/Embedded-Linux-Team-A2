#!/usr/bin/python3
from time import *
import pyautogui as gui


gui.hotkey('win')
sleep(0.5)
gui.write("Brave")
sleep(1)
gui.hotkey("enter")
sleep(1)
gui.hotkey('ctrl','n')
sleep(1)
gui.write("https://mail.google.com/mail/")
gui.hotkey("enter")
sleep(2)
#we can add here afew steps with pyautogui.prompt to add email & password 
checkbox = gui.locateCenterOnScreen("check.png", confidence = 0.8)
sleep(1)
gui.moveTo(checkbox)
gui.click(checkbox)
sleep(2)
checkbox = gui.locateCenterOnScreen("read.png", confidence = 0.8)
sleep(1)
gui.moveTo(checkbox)
gui.click(checkbox)
print("Done")
