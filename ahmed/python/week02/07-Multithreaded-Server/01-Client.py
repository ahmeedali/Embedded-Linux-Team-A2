#!/usr/bin/python3

import socket
# Socket connection(IP + port)
client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect(('127.0.1.1',5050)) 
 
print ("="*50)
while True:
    msg=input("Please enter message :")
    client1.send(msg.encode('UTF-8'))
    print ("="*50)
    data=client1.recv(1024)
    print(f"you recevied message :{data.decode('UTF-8')}")
    # if data.decode('UTF-8')=="bye":
    #     break
    client1.close()