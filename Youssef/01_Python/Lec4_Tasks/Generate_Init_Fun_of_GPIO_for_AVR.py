""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write python code to generate Init function of GPIO for AVR
"""

# Define a function to generate initialization code for GPIO (General-Purpose Input/Output).
def generate_gpio_init_code():
    
    # Create an empty list to store the DDRA (Data Direction Register A) bits.
    ddra_bits = []
    
    # Iterate through each bit position (0 to 7) for DDRA.
    for bit_position in range(8):
        
        # Prompt the user to input the mode (in or out) for the current bit.
        mode = input(f"Please enter Bit {bit_position} mode (in/out): ")
        
        # Check if the input mode is 'in' (input).
        if mode.lower() == "in":
            # Append '0' to the list for input mode.
            ddra_bits.append("0")
        # Check if the input mode is 'out' (output).
        elif mode.lower() == "out":
            # Append '1' to the list for output mode.
            ddra_bits.append("1")
        else:
            # Display an error message for invalid input and return None.
            print("Invalid input. Please enter 'in' or 'out'.")
            return None
    
    # Join the list of DDRA bits into a single string to create the DDRA value.
    ddra_value = ''.join(ddra_bits)
    
    # Return the DDRA value.
    return ddra_value

# Call the function to generate the DDRA initialization code.
ddra_code = generate_gpio_init_code()

# Check if the DDRA code is not None (valid input).
if ddra_code is not None:
    # Print the generated DDRA initialization code.
    print(f"DDRA = {ddra_code}")