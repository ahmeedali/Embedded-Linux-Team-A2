#Task: script for automating the installation of some vscode extensions using one command on your terminal if you have the needed python packages : 
import pyautogui as pg
import tkinter , sys
import os

def Locate(x):
 res=pg.locateCenterOnScreen(x,confidence=0.7) #may need to press maxmize first
 pg.click(res)
 print(res)
 pg.sleep(4)
 return res

os.popen('code')
Locate('maxmize.PNG')
pg.sleep(4)
ls=['clangd','helper','testmate']
try:
 Locate('Ext.PNG')
 pg.doubleClick(Locate('searchbox.PNG'))   
 for i in ls :      
       pg.typewrite(['backspace','enter'])   # ensure that the searchbox is empty before typing ..how to empty it not knowing the text length?
       pg.typewrite(i,interval=0.2)
       pg.sleep(4)
       Locate(i+'.PNG')
       Locate('installa.PNG')
       if (i == 'clangd'):
         pg.doubleClick(Locate('search_clang.PNG')) 
       if (i == 'helper'): 
         pg.doubleClick(Locate('search_helper.PNG')) 

except KeyboardInterrupt:
  print('\n')
