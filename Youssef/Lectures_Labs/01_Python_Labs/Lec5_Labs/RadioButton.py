import tkinter as tk

def on_radio_select():
    selected_option.set("Selected Option: " + selected_option.get())

# Create a tkinter window
window = tk.Tk()
window.title("Radio Button Example")
window.resizable(False,False)

# Create a StringVar to store the selected option
selected_option = tk.StringVar()

# Create radio buttons
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=selected_option, value="Option 1", command=on_radio_select)
radio_button2 = tk.Radiobutton(window, text="Option 2", variable=selected_option, value="Option 2", command=on_radio_select)
radio_button3 = tk.Radiobutton(window, text="Option 3", variable=selected_option, value="Option 3", command=on_radio_select)

# Set an initial selected option
selected_option.set("Option 1")

# Create a label to display the selected option
label = tk.Label(window, textvariable=selected_option)

# Arrange radio buttons and label using the grid layout manager
radio_button1.grid(row=0, column=0, padx=10, pady=5)
radio_button2.grid(row=1, column=0, padx=10, pady=5)
radio_button3.grid(row=2, column=0, padx=10, pady=5)
label.grid(row=3, column=0, padx=10, pady=5)

# Start the tkinter main loop
window.mainloop()
