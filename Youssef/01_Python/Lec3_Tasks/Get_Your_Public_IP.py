""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write application to get your public IP
"""

# Import the requests library, which allows us to make HTTP requests.
import requests

# Send an HTTP GET request to the URL to retrieve IP information.
URL = requests.get("https://api.ipify.org/?format=json")

# Print the content of the response received from the URL, which contains IP information in JSON format.
print(URL.text)
