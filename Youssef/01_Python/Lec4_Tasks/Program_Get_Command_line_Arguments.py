""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program to get the command-line arguments
"""

# Import the sys module, which provides access to command-line arguments.
import sys

# The first element in sys.argv (index 0) is the name of the script itself.
script_name = sys.argv[0]

# The rest of the elements in sys.argv (index 1 and beyond) are command-line arguments.
arguments = sys.argv[1:]

# Print the name of the script.
print(f"Script Name: {script_name}")

# Print a header for the list of command-line arguments.
print("Command-Line Arguments:")

# Iterate over the command-line arguments using enumerate to get both the index and value.
for i, arg in enumerate(arguments, start=1):
    # Print each command-line argument along with its position.
    print(f"Argument {i}: {arg}")