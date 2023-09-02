""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program to count the Number of Lines in a file.
"""

# Define a function to count the number of lines in a text file.
def count_lines(filename):
    
    try:
        # Attempt to open the file in read ('r') mode.
        with open(filename, 'r') as file:
            # Use a generator expression to count the lines efficiently.
            line_count = sum(1 for line in file)
        return line_count  # Return the count of lines in the file.

    except FileNotFoundError:
        return -1  # Indicates that the file was not found

# Prompt the user to enter the path to the text file.
file_name = input("Enter the path to the text file: ")

# Call the count_lines function to get the number of lines in the file.
num_lines = count_lines(file_name)

# Check if the number of lines is non-negative (file found).
if num_lines >= 0:
    # Print the number of lines in the file.
    print(f"The file '{file_name}' contains : {num_lines} lines.")
else:
    # Print a message indicating that the file was not found.
    print(f"File '{file_name}' not found.")