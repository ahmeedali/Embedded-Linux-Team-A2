""" 
   Autor      :     Youssef Adel Youssef
Description   :     Write a program that asks the user to type and return him its reverse
"""

import tkinter as tk

def reverse_word():
    # Get the word entered by the user
    word = entry_word.get()
    
    # Reverse the word
    reversed_word = word[::-1]
    
    # Display the reversed word in the label
    label_result.config(text=f"Reversed Word: {reversed_word}")

# Create a tkinter window
window = tk.Tk()
window.title("Word Reversal")
window.resizable(False,False)

# Create a label to instruct the user
label_instruction = tk.Label(window, text="Enter a word:")

# Create an entry field for the user to enter a word
entry_word = tk.Entry(window)

# Create a button to trigger word reversal
reverse_button = tk.Button(window, text="Reverse", command=reverse_word)

# Create a label to display the reversed word
label_result = tk.Label(window, text="Reversed Word: ")

# Arrange widgets using the grid layout manager
label_instruction.grid(row=0, column=0, padx=10, pady=5)
entry_word.grid(row=0, column=1, padx=10, pady=5)
reverse_button.grid(row=1, columnspan=2, padx=10, pady=10)
label_result.grid(row=2, columnspan=2, padx=10, pady=5)

# Start the tkinter main loop
window.mainloop()
