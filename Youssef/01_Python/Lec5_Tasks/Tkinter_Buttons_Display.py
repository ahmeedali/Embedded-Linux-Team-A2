""" 
   Autor      :     Youssef Adel Youssef
Description   :     Make this template and each button display different name
"""

import tkinter as tk

def button_click(button_num):
    label.config(text=f"Button {button_num} Clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Grid Example")
root.resizable(False,False)

# Create buttons
button1 = tk.Button(root, text="Button 1", command=lambda: button_click(1))
button2 = tk.Button(root, text="Button 2", command=lambda: button_click(2))
button3 = tk.Button(root, text="Button 3", command=lambda: button_click(3))
button4 = tk.Button(root, text="Button 4", command=lambda: button_click(4))

# Create a label to display button clicks
label = tk.Label(root, text="Click a button!")

# Use the grid layout manager to arrange buttons and label
button1.grid(row=0, column=1)
button2.grid(row=1, column=0)
button3.grid(row=1, column=2)
button4.grid(row=2, column=1)
label.grid(row=3, columnspan=3)

# Start the main GUI loop
root.mainloop()
