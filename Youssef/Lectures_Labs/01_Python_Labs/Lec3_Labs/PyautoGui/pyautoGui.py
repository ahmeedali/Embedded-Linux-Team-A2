""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write application to open terminal by using string or image compare
"""

import pyautogui
import os
import time

''' 
if you want to open terminal by string only 
'''

# pyautogui.hotkey('win')
# time.sleep(1)
# pyautogui.write('terminal')
# pyautogui.hotkey('enter')



''' 
if you want to open terminal by image compare
'''

pyautogui.hotkey('win')
time.sleep(1)
pyautogui.write('terminal')

mypath = os.path.dirname(os.path.realpath(__file__))+"/terminal.png"

isfind = None
while isfind is None:
    isfind = pyautogui.locateOnScreen(mypath)
    
print("i got the image")
pyautogui.hotkey('enter')