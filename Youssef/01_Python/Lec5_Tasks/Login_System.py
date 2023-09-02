""" 
   Autor      :     Youssef Adel Youssef
Description   :     Write a program for Login System
"""

# Import the tkinter library and the messagebox module from tkinter
import tkinter as tk
from tkinter import messagebox


# Define specific names allowed for login
allowed_names = {"youssef", "adel"}

# Function to handle the login button click
def login():
    
    # Get the first name and last name entered by the user
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()

    # Check if the combination of first name and last name is in the allowed_names set
    if first_name in allowed_names and last_name in allowed_names:
        # Display a success message using the messagebox.showinfo method
        messagebox.showinfo("Login Successful", f"Welcome, {first_name} {last_name}!")
    else:
        # Display an error message using the messagebox.showerror method
        messagebox.showerror("Login Error", "Invalid name combination. Please enter valid names.")


# Create a tkinter window
window = tk.Tk()
window.title("Login System")  # Set the window title
window.resizable(False, False)  # Disable window resizing

# Create labels for first name and last name
label_first_name = tk.Label(window, text="First Name:")
label_last_name = tk.Label(window, text="Last Name:")

# Create entry fields for first name and last name
entry_first_name = tk.Entry(window)
entry_last_name = tk.Entry(window)

# Create a login button and specify the function to be executed when clicked
login_button = tk.Button(window, text="Login", command=login)

# Arrange labels, entry fields, and the button using the grid layout manager
label_first_name.grid(row=0, column=0, padx=10, pady=5)
label_last_name.grid(row=1, column=0, padx=10, pady=5)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the tkinter main loop to display the window and handle user interactions
window.mainloop()