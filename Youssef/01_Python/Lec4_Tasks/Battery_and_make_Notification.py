""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program to print Battery percentage in Notification
"""

# Import the psutil library, which allows us to retrieve system information, including battery status.
import psutil

# Import the notification function from the plyer library, which is used for displaying notifications.
from plyer import notification

# Define a function to get the current battery percentage.
def get_battery_percentage():
    # Retrieve battery information using psutil and return the battery percentage.
    battery = psutil.sensors_battery()
    return battery.percent

# Check if this script is being run as the main program.
if __name__ == "__main__":
    # Get the current battery percentage using the defined function.
    battery_percent = get_battery_percentage()
    
    # Create a message with the battery percentage.
    message = f"Battery Percentage: {battery_percent}%"
    
    # Define the title and message for the notification.
    notification_title = "Battery Status"
    notification_message = message
    
    # Display a notification using the plyer library.
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name="Battery Notifier"
    )
