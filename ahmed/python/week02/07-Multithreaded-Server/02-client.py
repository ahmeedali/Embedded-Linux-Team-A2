#!/usr/bin/python3

import socket
# Socket connection(IP + port)
client2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
client2.connect((ip,8888)) 
 
print ("="*50)
while True:
    msg=input("Please enter message :")
    client2.send(msg.encode('UTF-8'))
    print ("="*50)
    data=client2.recv(1024)
    print(f"you recevied message :{data.decode('UTF-8')}")
    if data.decode('UTF-8')=="bye":
        client2.close()
        break
    else :
        continue
