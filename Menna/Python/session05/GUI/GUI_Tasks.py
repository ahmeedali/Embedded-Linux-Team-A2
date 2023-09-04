from tkinter import *
 
root = Tk()

def Led_on():
    oval = C.create_oval(150, 30, 250,150,fill="red")
    Label(root,text="Led is ON  ",font="Times 16 bold",fg="black",bg="burlywood1").place(x=158,y=200)

def Led_off():
    oval = C.create_oval(150, 30, 250,150,fill="maroon")
    Label(root,text="Led is OFF",font="Times 16 bold",fg="black",bg="burlywood1").place(x=155,y=200)


C = Canvas(root, bg="burlywood1",
           height=400, width=400)     
 #creating the circle
oval = C.create_oval(150, 30, 250,
                    150,
                     fill="red")
Label(root,text="Led is ON ",font="Times 16 bold",fg="black",bg="burlywood1").place(x=160,y=200)

button1 = Button(root,text="ON",fg="black",bg="light blue",width=25,command=Led_on)      #if these lines where placed above the canvas line
button2 = Button(root,text="OFF",fg="black",bg="light blue",width=25,command=Led_off)    #the button will not appear on it ..will be placed on background

button1.place(x=120,y=250,)
button2.place(x=120,y=300)

 
C.pack()
mainloop()    #as while loop to make the window running
