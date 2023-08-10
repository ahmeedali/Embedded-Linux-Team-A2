""" 
   Autor      :     Youssef Adel Youssef
Description   :     Write a Script to open a specific folder 
                    depending on Specific keys.
"""

import keyboard
import subprocess

def on_triggered():
   subprocess.run(['nautilus', '/home/youssef/Desktop/Tasks'])
   
def listen_for_shortcut():
   # Set the desired shortcut key combination (Ex : Ctrl + Alt + S)
   shortcut = "ctrl + alt + s"
   
   # Register the Callback function for the shortcut
   keyboard.add_hotkey(shortcut , on_triggered)
   
   # continuously listen for keyboard events
   keyboard.wait()
   

# Start Listening for the shortcut
listen_for_shortcut()