#!/usr/bin/python3

import socket
from threading import *


def client(c,add):
    while True:
        rodata = client.recv(1024)
        print(f"{add} sended {rodata.decode('UTF-8')}")
        msg = input(f" send to {add}: ")
        msg_encode = msg.encode('UTF-8')
        c.send(msg_encode)
        c.close()
  
srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
srv.bind((IP,5000))

#start server to listen 
srv.listen(5)
print(f"socket is listening to {IP}")
while True:
    c, add = srv.accept()
    print(f'Connected to :{add}')
    #start threading process
    thr =Thread(target=client,args=(c,add))
    thr.start()
    srv.close()

 
    
   
        
 
    