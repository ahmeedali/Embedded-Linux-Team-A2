#!/usr/bin/python3

import keyboard
import subprocess
import datetime


def on_triggered():
    print("triggered")
    fd = open("/home/ahmed/file.txt", "w")
    fd.write(str(datetime.datetime.now()))
    fd.close()


def listen_for_shortcut():
    # Set the desired shortcut key combination (Example: Ctrl + Alt + S)
    shortcut = "ctrl + alt + s"

    # Register the callback function for the shortcut
    keyboard.add_hotkey(shortcut, on_triggered)

    # Continuously listen for keyboard events
    keyboard.wait()


# Start listening for the shortcut
listen_for_shortcut()