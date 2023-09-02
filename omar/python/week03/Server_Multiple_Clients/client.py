import socket
host = '127.0.0.1'
port = 1234

def start_client(host, port):
    clientSocket = socket.socket()
    print('Waiting for connection')
    try:
        clientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    response = clientSocket.recv(2048)

    while True:
        client_send(client_socket=clientSocket)
        client_receive(client_socket=clientSocket)
        closeMessage = input("If you want to exit press Y/y or anything else to continue\n").upper()
        
        if closeMessage == 'Y':
            clientSocket.send(str.encode('exit'))
            break
    clientSocket.close()


def client_send(client_socket):
    message = input('Your message: ')
    client_socket.send(str.encode(message))

def client_receive(client_socket):
    response = client_socket.recv(2048)
    print(response.decode('utf-8'))


def main():
    start_client(host, port)
    
if __name__ == '__main__':
    main()