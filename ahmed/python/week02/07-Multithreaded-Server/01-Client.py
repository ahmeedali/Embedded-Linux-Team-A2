#!/usr/bin/python3

import socket
# Socket connection(IP + port)
client1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
client1.connect((ip,8888)) 
 
print ("="*50)

while True:
    msg=str(input("Please enter message :"))
    msg_encode= msg.encode('UTF-8')
    client1.send(msg_encode)
    print ("="*50)
    data=client1.recv(1024)
    print(f"you recevied message :{data.decode('UTF-8')}")
    print ("="*50)
    if data.decode('UTF-8')=="bye":
        client1.close()
        break
    else :
        continue
