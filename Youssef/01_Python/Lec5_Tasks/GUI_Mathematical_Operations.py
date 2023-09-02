""" 
   Autor      :     Youssef Adel Youssef
Description   :     Create a graphical application in Python Tkinter that asks
                    the user to enter two integers and displays their sum
"""

# Import the tkinter library and its ttk module for themed widgets
import tkinter as tk
from tkinter import ttk

# Function to calculate and display the result
def calculate_result():
    
    try:
        # Get the values from the entry fields and operation dropdown
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        operation = operation_var.get()

        # Perform the selected operation
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        else:
            result = "Invalid Operation"

        # Display the result in the result_label
        result_label.config(text=f"Result: {result}")
    
    except ValueError:
        # Handle the case where invalid integers are entered
        result_label.config(text="Please enter valid integers.")

# Create a tkinter window
window = tk.Tk()
window.title("Calculator")  # Set the window title
window.resizable(False, False)  # Disable window resizing

# Create labels
label_num1 = tk.Label(window, text="Enter the first number:")
label_num2 = tk.Label(window, text="Enter the second number:")

# Create entry fields
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)

# Create a dropdown for the operation
operation_var = tk.StringVar()
operation_label = tk.Label(window, text="Select Operation:")
operation_dropdown = ttk.Combobox(window, textvariable=operation_var, values=["Addition", "Subtraction"])
operation_dropdown.set("Addition")  # Set the default selected operation

# Create a calculate button with the calculate_result function as the command
calculate_button = tk.Button(window, text="Calculate", command=calculate_result)

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")

# Arrange widgets using the grid layout manager
label_num1.grid(row=0, column=0, padx=10, pady=5)               # Label for the first number
entry_num1.grid(row=0, column=1, padx=10, pady=5)               # Entry field for the first number
label_num2.grid(row=1, column=0, padx=10, pady=5)               # Label for the second number
entry_num2.grid(row=1, column=1, padx=10, pady=5)               # Entry field for the second number
operation_label.grid(row=2, column=0, padx=10, pady=5)          # Label for operation selection
operation_dropdown.grid(row=2, column=1, padx=10, pady=5)       # Dropdown for operation
calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)    # Calculate button
result_label.grid(row=4, columnspan=2, padx=10, pady=5)         # Label for displaying result

# Start the tkinter main loop to display the window
window.mainloop()

