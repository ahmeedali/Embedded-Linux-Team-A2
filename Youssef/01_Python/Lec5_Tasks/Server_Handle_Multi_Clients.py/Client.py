""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program to Create server receive multiple clients
"""

import socket
import time
import json
import random

while True:
    # Configure the client
    server_host = '127.0.0.1'  # Server's IP address or hostname
    server_port = 5000

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Generate a random value for the "Value" field
    random_value = random.randint(0, 1000)

    # Create a JSON message with the random value
    message = {
        "id": "XYZ",
        "Value": random_value,
        "type": "Temp"
    }

    # Convert the message to a JSON string
    message_json = json.dumps(message)

    # Send the JSON message to the server
    client_socket.send(message_json.encode('utf-8'))

    # Sleep to simulate multiple clients sending messages
    time.sleep(1)

    # Close the client socket
    client_socket.close()

    # Print a message to indicate the client received the message
    print("I got the message")
