""" 
   Autor      :   Youssef Adel Youssef
Description   :   Write a Python program to Create server receive multiple clients
"""

# Import necessary libraries
import socket
import threading

# Function to handle each client
def handle_client(client_socket, client_id):
    try:
        # Get the client's address
        client_addr = client_socket.getpeername()
        print(f"Accepted connection from {client_addr[0]}:{client_addr[1]} (Client {client_id})")

        while True:
            # Receive data from the client (up to 1024 bytes at a time)
            data = client_socket.recv(1024)
            
            # If no data is received, the client disconnected
            if not data:
                break

            # Process the received data from clients
            print(f"Received data from Client {client_id}: {data.decode('utf-8')}")

    except Exception as e:
        print(f"Client {client_id} Error: {str(e)}")
    finally:
        # Close the client socket when done handling the client
        client_socket.close()
        print(f"Client {client_id} disconnected.")


# Configure the server
server_host = '127.0.0.1'  # Listen on all available network interfaces
server_port = 5000

# Create a server socket (IPv4, TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the specified host and port
server.bind((server_host, server_port))

# Listen for incoming client connections with a queue size of 5
server.listen(5)

# Print a message indicating that the server is listening
print(f"Server listening on {server_host}:{server_port}")


# Create and handle three clients
client_count = 0
while True:
    # Accept a client connection, returning a client socket and client address
    client_sock, client_addr = server.accept()
    
    # Increment the client count
    client_count += 1
    
    # Start a new thread to handle the client using the handle_client function
    client_handler = threading.Thread(target=handle_client, args=(client_sock, client_count))
    client_handler.start()
