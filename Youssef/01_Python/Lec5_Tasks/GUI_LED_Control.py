""" 
   Autor      :     Youssef Adel Youssef
Description   :     Write a program to Control LED by GUI
"""

import tkinter as tk

# Function to turn the LED on (change circle color to red) and update the state label
def turn_led_on():
    circle_canvas.itemconfig(circle, fill="red")
    state_label.config(text="LED is ON")

# Function to turn the LED off (change circle color to white) and update the state label
def turn_led_off():
    circle_canvas.itemconfig(circle, fill="white")
    state_label.config(text="LED is OFF")

# Create a tkinter window
window = tk.Tk()
window.title("LED Control")

# Create a canvas to draw the circle
circle_canvas = tk.Canvas(window, width=100, height=100)
circle = circle_canvas.create_oval(20, 20, 80, 80, fill="white")

# Create buttons to control the LED
button_on = tk.Button(window, text="Turn On", command=turn_led_on)
button_off = tk.Button(window, text="Turn Off", command=turn_led_off)

# Create a label to display the LED state
state_label = tk.Label(window, text="LED is OFF")

# Arrange widgets using the grid layout manager
circle_canvas.grid(row=0, column=0, padx=10, pady=10)
button_on.grid(row=1, column=0, padx=10, pady=5)
button_off.grid(row=2, column=0, padx=10, pady=5)
state_label.grid(row=3, column=0, padx=10, pady=5)

# Start the tkinter main loop
window.mainloop()
