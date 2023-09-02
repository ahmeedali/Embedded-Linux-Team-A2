""" 
   Autor      :     Youssef Adel Youssef
Description   :     Write a program in Python that displays a window to the user that asks them to 
                    enter an integer N and displays its factorial
"""

# Import the tkinter library and its messagebox module
import tkinter as tk
from tkinter import messagebox

# Function to calculate the factorial
def calculate_factorial():
    
    try:
        # Get the integer value entered by the user in the entry field
        n = int(entry_n.get())

        # Check if the entered value is non-negative
        if n < 0:
            # Show an error message if the value is negative
            messagebox.showerror("Error", "Please enter a non-negative integer.")
        else:
            # Calculate the factorial of the entered integer
            result = 1
            for i in range(1, n + 1):
                result *= i
            # Display the factorial result in the result_label
            result_label.config(text=f"Factorial of {n}: {result}")
    except ValueError:
        # Show an error message if the entered value is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")


# Create a tkinter window
window = tk.Tk()
window.title("Factorial Calculator")  # Set the window title

# Create a label to instruct the user
label_instruction = tk.Label(window, text="Enter an integer N:")

# Create an entry field for the user to enter N
entry_n = tk.Entry(window)

# Create a button to calculate the factorial, set the command to call calculate_factorial
calculate_button = tk.Button(window, text="Calculate Factorial", command=calculate_factorial)

# Create a label to display the result
result_label = tk.Label(window, text="Factorial result will be displayed here.")


# Arrange widgets using the grid layout manager
label_instruction.grid(row=0, column=0, padx=10, pady=5)  # Label for instruction
entry_n.grid(row=0, column=1, padx=10, pady=5)  # Entry field
calculate_button.grid(row=1, columnspan=2, padx=10, pady=10)  # Calculate button
result_label.grid(row=2, columnspan=2, padx=10, pady=5)  # Label for displaying result


# Start the tkinter main loop to display the window
window.mainloop()

