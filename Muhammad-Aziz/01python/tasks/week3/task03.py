#! /usr/bin/python3

#Write a program that Apply summation, subtraction, dividing and multiplication operations on 2 numbers

from tkinter import *

task03 = Tk()
task03.title("Calculator")
task03.geometry("500x500+300+300")
task03.resizable(False,False)


def calc():
   result = 5
   global v
   if v.get() == 1:
      result = int(Op1.get())+ int(Op2.get())
   elif v.get() == 2:
      result = int(Op1.get()) - int(Op2.get())

   elif v.get() == 3:
      result = int(Op1.get()) * int(Op2.get())

   elif v.get() == 4:
      result = round(int(Op1.get()) / int(Op2.get()),3)
   print(v)
   Result.config(text=result)

label1 = Label(task03, width= 10, height= 2, text="Operand 1")
label2 = Label(task03, width= 10, height= 2, text="Operand 2")
label3 = Label(task03, width= 10, height= 2, text="Result")


Op1 = Entry(task03,fg="black", bg="white",width= 10)
Op2 = Entry(task03,fg="black", bg="white",width= 10)

CalcButton = Button(task03, fg="black", bg="grey",width= 4, height= 1, text = "Calc", command=calc)

Result = Label(task03, width= 10, height= 1,fg="black", text="")

v = IntVar()

sum = Radiobutton(task03,text="Sum",variable=v,value=1)
sub = Radiobutton(task03,text="Sub",variable=v,value=2)
mul = Radiobutton(task03,text="Mul",variable=v,value=3)
div = Radiobutton(task03,text="Div",variable=v,value=4)

label1.place(x= 100,y=55)
label2.place(x= 100,y=100)
label3.place(x= 100,y=145)

Op1.place(x=200,y=60)
Op2.place(x=200,y=105)
Result.place(x=200,y=150)

CalcButton.place(x=200,y=210)

sum.place(x=350,y=50)
sub.place(x=350,y=85)
mul.place(x=350,y=120)
div.place(x=350,y=155)


task03.mainloop()