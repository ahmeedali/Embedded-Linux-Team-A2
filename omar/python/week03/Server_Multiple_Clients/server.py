import socket
from _thread import *

host = '127.0.0.1'
port = 1234

def client_handler(connection, address):
    connection.send(str.encode('You are now connected to the replay server...'))
    while True:
        data = connection.recv(2048)    # __bufsize = 2048
        message = data.decode('utf-8')
        if message == 'exit':
            print(f'Client({address[0]}:{str(address[1])}) disconnected')
            break
        reply = f'Server: {message}'
        connection.sendall(str.encode(reply))
        print(f'Client({address[0]}:{str(address[1])}): {str(message)}')
    connection.close()

def accept_connections(ServerSocket):
    client, address = ServerSocket.accept()

    # Print client host address and port
    print(f'Connected to: {address[0]}:{str(address[1])}')
    start_new_thread(client_handler, (client, address, )) 

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)

def main():
    start_server(host, port)

if __name__ == '__main__':
    main()