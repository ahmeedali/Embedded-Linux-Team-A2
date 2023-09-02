import pyautogui

# Get the current x and y coordinates of the mouse pointer
while True:
    x, y = pyautogui.position() 
    print(f"Mouse position - X: {x}, Y: {y}")