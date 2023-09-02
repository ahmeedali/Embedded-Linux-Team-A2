#!/usr/bin/python3

import socket
# Socket connection(IP + port)
client2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client2.connect(('127.0.1.1',5050)) 
 
print ("="*50)
while True:
    msg=input("Please enter message :")
    client2.send(msg.encode('UTF-8'))
    print ("="*50)
    data=client2.recv(1024)
    print(f"you recevied message :{data.decode('UTF-8')}")
    client2.close()
    