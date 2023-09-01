#!/usr/bin/python3
from tkinter import *
from math import factorial as fc

window = Tk()
window.title('Factorial')
window.geometry("400x90+400+250")
window.resizable(False,False)

Var = StringVar()
Var.set('')

def factorial():
    val = int(number.get())
    Var.set(f'The factorial of {val} is {val}! = {fc(val)}')
    window.update_idletasks

lb1 = Label(window,text="Enter value of integer N : ")
output = Label(window,textvariable=Var)
number = Entry(window)
validateButton = Button(window,text="Validate",fg="black",bg="white",command=factorial)

lb1.grid(row=0,column=0)
output.grid(row=1,column=1)
number.grid(row=0,column=1)
validateButton.grid(row=3,column=1)

window.mainloop()