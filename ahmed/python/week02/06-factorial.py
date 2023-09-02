#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import math
def Factorial():
    num = int(entry.get())
    fact= math.factorial(num)
    messagebox.showinfo("Factorial Reslut" , message=f"Factorial of {num} = {fact}")
    entry.delete(0, END)

f = Tk()
f.title("Factorial Calculator") 
f.geometry("300x200")    
f.resizable(0,0)

#create options
label = Label(f, text = "Enter value of integer N",height=2, font=("Arial", 16))
entry = Entry(f)
button = Button(f, text = "Calculate", command =Factorial)

#packing
label.pack(padx=0, pady=0)
entry.pack(padx=0, pady=20)
button.pack(padx=20, pady=20)

f.mainloop()


