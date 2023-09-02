#!/usr/bin/python3
from tkinter import *

window = Tk()
window.title('Reverse Text')
window.geometry("260x80+400+250")
window.resizable(False,False)

def reverse_text():
    text = entry.get()
    revText = text[::-1]
    print(revText)
    reversedText = Label(window,text=revText)
    reversedText.grid(row=1,column=1)

reqText = Label(window,text="Enter a word:")
reversedText = Label(window,text="")
entry = Entry(window)
validateButton = Button(window,text="Validate",fg="black",bg="white",command=reverse_text)

reqText.grid(row=0,column=0)
reversedText.grid(row=1,column=1)
entry.grid(row=0,column=1)
validateButton.grid(row=3,column=1)

window.mainloop()