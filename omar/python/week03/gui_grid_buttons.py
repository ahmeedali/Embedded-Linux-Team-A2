#!/usr/bin/python3
from tkinter import *

window = Tk()
window.title('Grid Buttons')
window.geometry("240x95+300+200")
window.resizable(False,False)

b1 = Button(window,text="Button1",fg="white",bg="black")
b2 = Button(window,text="Button2",fg="white",bg="black")
b3 = Button(window,text="Button3",fg="white",bg="black")
b4 = Button(window,text="Button4",fg="white",bg="black")

b1.grid(row=0,column=1)
b2.grid(row=1,column=0)
b3.grid(row=1,column=2)
b4.grid(row=2,column=1)

window.mainloop()