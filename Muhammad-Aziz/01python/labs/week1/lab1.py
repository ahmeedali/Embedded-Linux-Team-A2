#! /usr/bin/python3


#Lab (Add shortcuts or running CLI commands using Python Scripts)
import keyboard
import subprocess

def on_trigger():
    subprocess.run('nautils, /home/muhammadz99')

def listen_for_shortcut():
    shortcut = 'ctrl + alt + s'
    keyboard.add_hotkey(shortcut,on_trigger)
    keyboard.wait()

listen_for_shortcut()