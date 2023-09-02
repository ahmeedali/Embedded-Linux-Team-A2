#!/usr/bin/python3
from tkinter import *

window = Tk()
window.title('Led State')
window.geometry("400x300+400+250")
window.configure(background="grey")
window.resizable(False,False)

var = StringVar()
var.set('Led is off')

myCanvas = Canvas(width=150, height=150, bg="grey")
myCanvas.pack()

def led_on():
    myCanvas.itemconfig(led, fill="green")
    var.set('Led is on')
    window.update_idletasks

def led_off():
    myCanvas.itemconfig(led, fill="white")
    var.set('Led is off')   
    window.update_idletasks

output = Label(window,textvariable=var)
onButton = Button(window,text="Led On",fg="black",bg="white",command=led_on)
offButton = Button(window,text="Led Off",fg="black",bg="white",command=led_off)
led = myCanvas.create_oval(150,50,50,150, width=3, fill="white")

output.pack()
onButton.pack()
offButton.pack()

window.mainloop()