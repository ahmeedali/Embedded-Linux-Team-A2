""" 
   Autor      :     Youssef Adel Youssef
Description   :     Python program to parse header file and read all prototypes of function 
                    and insert it into excel sheet with unique ID start with IDX0
"""

# Import necessary libraries
import re           # Regular expression library for pattern matching
import openpyxl     # Library for working with Excel files


# Define a function to extract function prototypes from a header file
def extract_function_prototypes(header_file):
    
    # Open the header file for reading
    with open(header_file, 'r') as file:
        content = file.read()  # Read the content of the file
    
    # Use regular expressions to find function prototypes and store them in a list
    prototypes = re.findall(r'\w+\s+\w+\s*\([^)]*\);', content)
    return prototypes  # Return the list of function prototypes


# Define a function to create an Excel sheet and insert function prototypes
def create_excel_sheet(prototypes):
    
    wb = openpyxl.Workbook()                # Create a new Excel workbook
    sheet = wb.active                       # Get the active sheet in the workbook
    sheet.title = 'Function Prototypes'     # Set the sheet title
    
    sheet['A1'] = 'ID'                      # Set the header for the ID column
    sheet['B1'] = 'Prototype'               # Set the header for the Prototype column
    
    # Loop through the list of function prototypes and insert them into the sheet
    for idx, prototype in enumerate(prototypes, start=1):
        cell_id = f"IDX{idx - 1}"           # Generate a unique ID for each prototype
        sheet[f'A{idx + 1}'] = cell_id      # Insert the ID in the 'A' column
        sheet[f'B{idx + 1}'] = prototype    # Insert the prototype in the 'B' column
    
    wb.save('function_prototypes.xlsx')     # Save the workbook as 'function_prototypes.xlsx'


# Entry point of the program
if __name__ == "__main__":
    header_file = './Header_File.h'  # Specify the path to the header file
    prototypes = extract_function_prototypes(header_file)  # Extract prototypes
    
    if prototypes:
        create_excel_sheet(prototypes)  # Create Excel sheet with prototypes
        print("Function prototypes inserted into 'function_prototypes.xlsx'")
    else:
        print("No function prototypes found in the header file.")