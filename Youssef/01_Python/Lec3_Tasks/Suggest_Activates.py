""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a code to suggest automatically activates for you
"""

# Import the `sleep` function from the `time` module, which allows us to pause execution for a specified number of seconds.
from time import sleep

# Import the `requests` library, which is used for making HTTP requests.
import requests

# Create an infinite loop to repeatedly fetch random activities.
while True:
   
    # Send an HTTP GET request to the URL to get a random activity.
    URL = requests.get("https://www.boredapi.com/api/activity")

    # Print the randomly fetched activity from the JSON response.
    print(URL.json()['activity'])

    # Pause the program for 2 seconds before fetching the next activity.
    sleep(2)