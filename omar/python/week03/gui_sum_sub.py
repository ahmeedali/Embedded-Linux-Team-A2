#!/usr/bin/python3
from tkinter import *

window = Tk()
window.title('Simple Calculator')
window.geometry("340x100+400+250")
window.resizable(False,False)

def calculate():
    global selectVar
    out = 0
    n1 = int(num1.get())
    n2 = int(num2.get())
    operation = int(selectVar.get())
    print(operation)
    if operation == 1:
        out = n1 + n2
    elif operation == 2:
        out = n1 - n2
    else:
        out = 0

    output = Label(window,text=str(out))
    output.grid(row=2,column=1)

lb1 = Label(window,text="Enter the first number: ")
lb2 = Label(window,text="Enter the second number:")
output = Label(window,text="")
num1 = Entry(window)
num2 = Entry(window)

selectVar = IntVar()
sum = Radiobutton(window,text="Sum",variable=selectVar,value=1)
sub = Radiobutton(window,text="Sub",variable=selectVar,value=2)
ValidateButton = Button(window,text="Validate",fg="black",bg="white",command=calculate)

lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)
output.grid(row=2,column=1)
num1.grid(row=0,column=1)
num2.grid(row=1,column=1)
sum.grid(row=2,column=0)
sub.grid(row=3,column=0)
ValidateButton.grid(row=3,column=1)

window.mainloop()