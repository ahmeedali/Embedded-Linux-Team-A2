""" 
   Autor      :   Youssef Adel Youssef
Description   :   Using “Pyautogui” to open Emails and change Emails from unread to read
"""

# Import the necessary libraries
import pyautogui     # For automating GUI interactions
import time          # For adding delays in the script

# Press the Windows key to open the Start menu
pyautogui.hotkey('win')

# Wait for 3 seconds to allow time for the Start menu to open
time.sleep(3)

# Type 'firefox' into the Start menu search and press Enter to open Firefox (assuming Firefox is installed)
pyautogui.write('firefox')
pyautogui.hotkey('enter')

# Wait for a few seconds for Firefox to open
time.sleep(3)

# Open a new tab in the browser by pressing Ctrl + T
pyautogui.hotkey('ctrl', 't')

# Type the URL into the browser's address bar and press Enter
pyautogui.typewrite('https://mail.google.com')
pyautogui.press('enter')

# Wait for 5 seconds for the Gmail page to load
time.sleep(5)

# Simulate clicking on the first email in the list. Adjust the coordinates based on your screen resolution.
pyautogui.click(x=350, y=300)

# Wait for 3 seconds to allow the email to open
time.sleep(3)

# Simulate clicking the "Mark as Read" button. Adjust the coordinates based on your screen resolution.
pyautogui.click(x=560, y=200)

# If you need to close the browser tab, you can use the following line (not included in the original code)
# pyautogui.hotkey('ctrl', 'w')





# to Adjust coordinates based on your screen
# Get the current x and y coordinates of the mouse pointer by the under code
# while True:
#     x, y = pyautogui.position() 
#     print(f"Mouse position - X: {x}, Y: {y}")
