#! /usr/bin/python3

#Make this template(Square shape) and each button display different name

from tkinter import *

task01 = Tk()
task01.title("Calculator")
task01.geometry("500x500+300+300")
task01.resizable(False,False)


def Up():
    print("Up Button is Pressed")
def Down():
    print("Down Button is Pressed")
def Right():
    print("Right Button is Pressed")
def Left():
    print("Left Button is Pressed")

UpButton = Button(task01, fg="black", bg="grey",width= 4, height= 1, text = "Up", command=Up)
DownButton = Button(task01, fg="black", bg="grey",width= 4, height= 1, text = "Down", command=Down)
RightButton = Button(task01, fg="black", bg="grey",width= 4, height= 1, text = "Right", command=Right)
LeftButton = Button(task01, fg="black", bg="grey",width= 4, height= 1, text = "Left", command=Left)

UpButton.place(x=200,y=40)
DownButton.place(x=200,y=120)
RightButton.place(x=120,y=80)
LeftButton.place(x=280,y=80)



task01.mainloop()