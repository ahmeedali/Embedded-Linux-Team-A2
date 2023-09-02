""" 
   Autor      :   Youssef Adel Youssef
Description   :   write a Python program to count the Number of words in a file.
"""

# Define a function to count words in a text file
def count_words(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Split the content into words based on spaces
            word_count = len(content.split())
        return word_count  # Return the word count
    
    except FileNotFoundError:
        return -1  # Indicates that the file was not found


# Prompt the user to enter the path to the text file
file_name = input("Enter the path to the text file: ")

# Call the count_words function to count words in the file
num_words = count_words(file_name)


# Check if the word count is non-negative (file exists)
if num_words >= 0:
    # Print the word count and the file name
    print(f"The file '{file_name}' contains: {num_words} words.")
else:
    # Print a message indicating that the file was not found
    print(f"File '{file_name}' not found.")
