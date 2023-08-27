#! /usr/bin/python3

'''
Using PyAutoGUI 
- To open vscode 
- install clangd from extension
- install c++ testmate  from extension
- install c++ helper  from extension
- install cmake  from extension
- install cmake tools  from extension
'''

import pyautogui as pag
import time


def init_vs():
    pag.hotkey("win")
    time.sleep(1)
    pag.typewrite('v')
    time.sleep(1)
    pag.hotkey("enter")
    time.sleep(1)


def clangd():
    pag.hotkey('ctrl','shift','x')
    time.sleep(1)
    pag.hotkey('ctrl','a')
    time.sleep(1)
    pag.hotkey('delete')
    pag.typewrite('clangd')
    time.sleep(2)

def cpp_testmate():
    time.sleep(1)
    pag.hotkey('ctrl','shift','x')
    time.sleep(1)
    pag.hotkey('ctrl','a')
    time.sleep(1)
    pag.hotkey('delete')
    pag.typewrite('c++ test')
    time.sleep(2)

    
def cpp_helper():
    time.sleep(1)    
    pag.hotkey('ctrl','shift','x')
    time.sleep(1)
    pag.hotkey('ctrl','a')
    time.sleep(1)
    pag.hotkey('delete')
    pag.typewrite('c++ helper')
    time.sleep(2)


def cmake():
    time.sleep(1)
    pag.hotkey('ctrl','shift','x')
    time.sleep(1)
    pag.hotkey('ctrl','a')
    time.sleep(1)
    pag.hotkey('delete')
    pag.typewrite('cmake')
    time.sleep(2)

def cmake_tools():
    time.sleep(1)
    pag.hotkey('ctrl','shift','x')
    time.sleep(1)
    pag.hotkey('ctrl','a')
    time.sleep(1)
    pag.hotkey('delete')
    pag.typewrite('cmake tools')
    time.sleep(2)
    
def pointer_move():
    pointxy = None
    if pointxy is None:
        print(pag.position())
        time.sleep(2)
        pointxy = pag.moveTo(2129,179)        
        time.sleep(2)
        pointxy = pag.position()
        time.sleep(2)
        pag.click()
        print(pointxy)
        time.sleep(2)
        pointxy = pag.moveTo(2752,230)
        time.sleep(2)
        pag.click()
        time.sleep(1)



init_vs()
clangd()
pointer_move()
cpp_testmate()
pointer_move()
cpp_helper()
pointer_move()
cmake()
pointer_move()
cmake_tools()
pointer_move()