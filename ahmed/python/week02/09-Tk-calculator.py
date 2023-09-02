#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox

opertaions = Tk()
opertaions.title('Calculator')
opertaions.geometry("300x150")
opertaions.resizable(0,0)

def calculate():
    n1 = int(num1.get())
    n2 = int(num2.get())
    
    if v.get() == 'sum':
        r = n1 + n2
    elif v.get() == 'sub':
        r = n1 - n2
         
    messagebox.showinfo("Reslut" , message=f"Reslut of operation = {r}")
    num1.delete(0, END)
    num2.delete(0, END)
    
v = StringVar()


sum = Radiobutton(opertaions,text="Sum",variable=v,value='sum')
sub = Radiobutton(opertaions,text="Sub",variable=v,value='sub')
cal = Button(opertaions,text="Calculate",bg="white",command=calculate)

lb1 = Label(opertaions,text="Enter 1st number: ")
lb2 = Label(opertaions,text="Enter 2nd number:")
num1 = Entry(opertaions)
num2 = Entry(opertaions)


lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)
num1.grid(row=0,column=1)
num2.grid(row=1,column=1)
sum.grid(row=5,column=0)
sub.grid(row=6,column=0)
cal.grid(row=4,column=1)

opertaions.mainloop()

