#! /usr/bin/python3

#Write a program that asks the user to type a number and returns its factorial

from tkinter import *

task06 = Tk()
task06.title("Factorial")
task06.geometry("500x500+300+300")
task06.resizable(False,False)

def fac():
    result = 1
    counter = int(Op1.get())
    while counter != 1:
        result *= counter
        counter -= 1
    Result.config(text=f"Factorial of {Op1.get()} = "+str(result))

label1 = Label(task06, width= 10, height= 2, text="Number")
label2 = Label(task06, width= 10, height= 2, text="Result:")

Op1 = Entry(task06,fg="black", bg="white",width= 10)

CalcButton = Button(task06, fg="black", bg="grey",width= 4, height= 1, text = "Calc", command=fac)

Result = Label(task06, width= 25, height= 1,fg="black", text="")

label1.place(x= 100,y=55)
label2.place(x= 100,y=100)

Op1.place(x=200,y=60)
Result.place(x=165,y=105)

CalcButton.place(x=200,y=210)


task06.mainloop()