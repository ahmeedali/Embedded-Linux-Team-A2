import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received from client : {data}")
        num=10
        # Send a response back to the client
        response = f"the temperature is : {num}"
        client_socket.send(response.encode('utf-8'))

    # Close the client socket
    print("client closed from server..")
    print("=========================================")
    client_socket.close()

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip=socket.gethostbyname(socket.gethostname()) 
    # Bind the socket to a specific address and port
    server_address = (ip, 12345)
    server_socket.bind(server_address)
    server_socket.settimeout(3*60)                                  # times out after 3 min of no clients
    # Listen for incoming connections
    server_socket.listen(5)
    print("Server is listening for connections...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))  #to serve each client in parallel with other clients
        client_thread.start()

start_server()