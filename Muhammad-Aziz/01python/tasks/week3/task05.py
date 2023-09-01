#! /usr/bin/python3

# led on / led off task

from tkinter import *
 
def led_on():
    canvas.itemconfig(Led,fill='red')
    LedStatus.config(text="Led is ON")
def led_off():
    canvas.itemconfig(Led,fill='white')
    LedStatus.config(text="Led is OFF")

 
     

# Create the main task05
task05 = Tk()

# Create a Canvas widget
canvas = Canvas(task05, width=400, height=400)
canvas.pack()

# Draw a circle and fill it
x1, y1 = 150, 150  # Top-left corner of the bounding box
x2, y2 = 250, 250  # Bottom-right corner of the bounding box
Led = canvas.create_oval(x1, y1, x2, y2, fill='white')
LedOn = Button(task05, fg="black", bg="grey",width= 4, height= 1, text = "ON", command=led_on)
LedOff = Button(task05, fg="black", bg="grey",width= 4, height= 1, text = "OFF", command=led_off)
LedStatus = Label(task05, width= 10, height= 2, text="")

LedOn.place(x=175,y=320)
LedOff.place(x=175,y=360)
LedStatus.place(x=175,y=280)
# Start the application
task05.mainloop()