import tkinter as tk

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index[0])
        label.config(text=f"Selected Item: {selected_item}")

# Create a tkinter window
window = tk.Tk()
window.title("Listbox Bind Example")
window.resizable(False,False)

# Create a Listbox widget with some items
listbox = tk.Listbox(window)
listbox.pack()

items = ["Python", "Java", "C", "C++", "Rust"]
for item in items:
    listbox.insert(tk.END, item)

# Create a label to display the selected item
label = tk.Label(window, text="Selected Item: ")
label.pack()

# Bind the Listbox to the selection event
listbox.bind("<<ListboxSelect>>", on_select)

# Start the tkinter main loop
window.mainloop()
