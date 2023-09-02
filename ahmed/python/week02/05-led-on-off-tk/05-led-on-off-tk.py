#!/usr/bin/python3
from tkinter import *

#functions for creating configuration for button and label 

def ledoff ():
    switch.configure(file="off.png")
    sw_bt.configure(command=ledon)
    lb_led.configure(image=off)
    
def ledon (): 
    switch.configure(file="on.png") 
    sw_bt.configure(command=ledoff) 
    lb_led.configure(image=on)
          
# create window with default settings       
root = Tk()
root.geometry("400x600")
root.configure(background="#2a2f3b")
root.resizable(0, 0)
root.title("led")

#add custom images
switch=PhotoImage(file="on.png")
on=PhotoImage(file="ledon.png")
off=PhotoImage(file="ledoff.png")

#creating label and button with command order 
lb_led=Label(root,image=on,bg="#2a2f3b")
sw_bt=Button(root,image=switch,command=ledoff,bd=0,bg="#2a2f3b",highlightthickness = 0,activebackground="#2a2f3b")

#packing buttons and labels
lb_led.pack()
sw_bt.pack(padx=50,pady=50)

#for looping 
root.mainloop()