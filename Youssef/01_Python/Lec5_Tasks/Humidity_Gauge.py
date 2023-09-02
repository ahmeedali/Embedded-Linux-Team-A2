""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program to Create Humidity Gauge
"""

# Import necessary libraries
import tkinter as tk
import math

# Function to create the half-circle gauge chart
def create_half_circle_gauge(canvas, value):
    # Clear the canvas
    canvas.delete("all")

    # Constants for the gauge and arcs
    center_x = canvas.winfo_reqwidth() // 2
    center_y = canvas.winfo_reqheight() // 2
    radius = min(center_x, center_y) - 10

    # Draw the green arc (0% to 80%)
    start_angle = 140  # Start at the top
    end_angle = 80
    canvas.create_arc(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        start=start_angle, extent=end_angle - start_angle,
        outline="green", width=30, style=tk.ARC
    )

    # Draw the yellow arc (80% to 90%)
    start_angle = 80
    end_angle = 60
    canvas.create_arc(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        start=start_angle, extent=end_angle - start_angle,
        outline="yellow", width=30, style=tk.ARC
    )

    # Draw the red arc (90% to 100%)
    start_angle = 60
    end_angle = 40
    canvas.create_arc(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        start=start_angle, extent=end_angle - start_angle,
        outline="red", width=30, style=tk.ARC
    )

    # Calculate the angle based on the value
    start_angle = 140  # Start at the top
    end_angle = 40
    angle = start_angle - (start_angle - end_angle) * value / 100

    # Calculate the position of the indicator line
    indicator_x = center_x + radius * 0.8 * math.cos(math.radians(angle))
    indicator_y = center_y - radius * 0.8 * math.sin(math.radians(angle))  # Negative to invert the arc

    # Draw the indicator line on the gauge with varying line width
    canvas.create_line(
        center_x, center_y,
        indicator_x, indicator_y,
        fill="black", width=6, capstyle=tk.ROUND
    )

    # Display the value as humidity
    humidity_text = "Humidity: "
    canvas.create_text(center_x, center_y + 60, text=humidity_text + f"{value}%", font=("Helvetica", 16))

    # Determine and display the state of the bar
    if value < 60:
        state = "Normal"
    elif 60 <= value < 80:
        state = "Medium"
    else:
        state = "High"
    
    state_text = "State: " + state
    canvas.create_text(center_x, center_y + 100, text=state_text, font=("Helvetica", 16), fill="red")

# Create the main window
root = tk.Tk()
root.title("Humidity")

# Create a canvas for the half circle gauge chart
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create a button to update the gauge
def update_gauge():
    value = float(entry_value.get())
    if 0 <= value <= 100:
        create_half_circle_gauge(canvas, value)
    else:
        entry_value.delete(0, tk.END)
        entry_value.insert(0, "Invalid")

update_button = tk.Button(root, text="Update Gauge", command=update_gauge)
update_button.pack()

# Create an entry field for the gauge value
entry_value = tk.Entry(root, width=10)
entry_value.pack()

# Initialize the gauge with a default value
create_half_circle_gauge(canvas, 50)

# Start the tkinter main loop
root.mainloop()
