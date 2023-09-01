#!/usr/bin/python3                                                                                                                                                                          

import socket              
import _thread

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        print (addr, ' >> ', msg)
        msg = input('SERVER >> ')
        msg_encoded = msg.encode('UTF-8')
        clientsocket.send(msg_encoded)
    clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 5000

print ('Server started!')
print ('Waiting for clients...')

s.bind((host, port))
s.listen(5)

while True:
   c, addr = s.accept()
   print ('Got connection from', addr)
   _thread.start_new_thread(on_new_client,(c,addr))
s.close()