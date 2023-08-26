import keyboard
from tkinter import Tk

root = Tk()
root.withdraw()

def save_clipboard_to_file():
    clipboard_text = root.clipboard_get()
    if clipboard_text:
        with open("notes.txt", "a") as file:
            file.write(clipboard_text + "\n")
        print("Copied text saved to notes.txt")

if __name__ == "__main__":
    print("Press Alt+Shift+S to save copied text to notes.txt")
    while True:
        keyboard.wait('shift+alt+s')
        save_clipboard_to_file()
