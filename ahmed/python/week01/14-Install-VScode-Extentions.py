#!/usr/bin/python3
from time import *
import pyautogui as gui
gui.confirm('Shall we proceed?')
sleep(1)
gui.hotkey('win')
sleep(0.5)
gui.write("terminator")
sleep(1)
gui.hotkey("enter")
sleep(0.5)
gui.write("code")
sleep(0.5)
gui.hotkey("enter")
sleep(3)
gui.hotkey('ctrl', 'shift', 'x')
sleep(0.5)
gui.hotkey("f11")
sleep(0.5)
 Ahmed-Ali
gui.click(270, 55, 1, button='left')
gui.write("code")
x, y = gui.locateCenterOnScreen('.png')
gui.click(x, y)

x, y = gui.locateCenterOnScreen('calc7key.png')
gui.click(x, y)

# while True:
#    x,y=gui.position()
#    print(x,y)


