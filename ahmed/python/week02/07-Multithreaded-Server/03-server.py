#!/usr/bin/python3

import socket
from threading import *


def client(c):
    while True:
        data = c.recv(1024)
        print(f"{add} sended {data.decode('UTF-8')}")
        print ("="*50)
        msg = input(f" send to {add}: ")
        msg_encode = msg.encode('UTF-8')
        c.send(msg_encode)
    c.close()
       

        
  
srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
srv.bind((IP,8888))

#start server to listen 
srv.listen(5)
print(f"socket is listening to {IP}")
while True:
    Csocket,add=srv.accept()
    print(f'Connected to :{add}')
    print ("="*50)
    #start threading process
    thr =Thread(target=client,args=(Csocket,))
    thr.start()
 



        
 
    