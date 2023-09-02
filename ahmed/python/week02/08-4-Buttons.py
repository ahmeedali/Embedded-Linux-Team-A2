#!/usr/bin/python3
from  tkinter import *



window= Tk()
window.title("Buttons")
window.geometry("240x100")



b1=Button(window,text="Button 1",bg="#2a2f3b",highlightthickness = 0)
b2=Button(window,text="Button 2",bg="#2a2f3b",highlightthickness = 0)
b3=Button(window,text="Button 3",bg="#2a2f3b",highlightthickness = 0)
b4=Button(window,text="Button 4",bg="#2a2f3b",highlightthickness = 0)


b1.grid(row=0,column=2)
b2.grid(row=1,column=0)
b3.grid(row=1,column=3)
b4.grid(row=2,column=2)

window.mainloop()