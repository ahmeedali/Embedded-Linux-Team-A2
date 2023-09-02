#!/usr/bin/python3

from tkinter import *

window = Tk()
window.title("Reverse Words")
window.geometry('300x100')
window.resizable(0,0)

def rev ():
   res=str(entry.get())[::-1]
   lb2.config(text = res)

lb1 = Label(window,text="Enter a word:")
entry = Entry(window)
lb2 = Label(window,text=" ")
vb = Button(window,text="Validate",command=rev)

lb1.grid(column=1,row=1)
entry.grid(column=2,row=1)
lb2.grid(column=2,row=3)
vb.grid(column=2,row=4)


window.mainloop()



