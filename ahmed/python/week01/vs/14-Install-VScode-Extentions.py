#!/usr/bin/python3
from time import *
import pyautogui as gui

def install_check ():
    if gui.locateCenterOnScreen('install.png',confidence=0.9)!= None:
        gui.moveTo (gui.locateOnScreen('install.png', confidence=0.9))
        gui.click(gui.locateCenterOnScreen('install.png', confidence=0.9))
        sleep(1)
        print ("Done")
    elif gui.locateCenterOnScreen('uninstall.png', confidence=0.9)!= None:
            print ("Extenation already installed")
            
        

gui.confirm('Shall we proceed?',)
sleep(1)
gui.hotkey('win')
sleep(0.5)
gui.write("vscode")
sleep(1)
gui.hotkey("enter")
sleep(2)
gui.hotkey('ctrl', 'shift', 'x')
gui.hotkey("f11")


tools = {"clangd":"clangd.png",
         "c++ testmate":"c++_testmate.png",
         "c++ helper":"c++_helper.png",
         "cmake":"cmake.png",
         "cmake tools":"cmake_tools.png"}      


for name ,img in tools.items():
    gui.click(270, 55, 1, button='left')
    sleep(1)
    gui.hotkey('ctrl', 'l')
    gui.hotkey('delete')
    sleep(1)
    gui.write(name)
    sleep(3)
    pos = gui.locateOnScreen(img, confidence=0.7)
    gui.moveTo(pos)
    gui.click(pos)
    sleep(4)
    install_check ()
gui.hotkey("f11")