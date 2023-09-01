#! /usr/bin/python3

#Write a program that asks the user to type a word and return him its reverse

from tkinter import *

def rev():
    result = str(Op1.get())[::-1]
    Result.config(text = result)


task02 = Tk()
task02.title("Calculator")
task02.geometry("500x500+300+300")
task02.resizable(False,False)

label1 = Label(task02, width= 10, height= 2, text="Enter A word")
label2 = Label(task02, width= 10, height= 2, text="Reversed Word")


Op1 = Entry(task02,fg="black", bg="white",width= 10)

Reverse = Button(task02, fg="black", bg="grey",width= 4, height= 1, text = "Reverse", command=rev)

Result = Label(task02, width= 10, height= 1,fg="black", text="")


label1.place(x= 100,y=55)
label2.place(x= 200,y=145)

Op1.place(x=200,y=60)
Result.place(x=200,y=150)

Reverse.place(x=200,y=210)

task02.mainloop()