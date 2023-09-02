""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program to write a “list” to a file
"""

# Create a list of colors
color = ['Red', 'Green', 'Blue', 'Black', 'White']

# Open a file named 'COLORS.txt' in write mode ('w') and use a context manager
# The 'with' statement ensures that the file is properly closed after writing
with open('COLORS.txt', "w") as Myfile:
    # Write the contents of the 'color' list to the file, separated by spaces
    Myfile.write(" ".join(color))

# Open the 'COLORS.txt' file for reading
content = open('COLORS.txt')

# Read the content of the file and print it
print(content.read())

# The 'with' statement automatically closes the file when it goes out of scope
