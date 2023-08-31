#To open a socket on any machine : socket(address) = ip(this machine) + port   socket1 0-------0 socket2
#ports available to use : 49152-65535– These are used by client programs 
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())       #you can use standard ip that indicates your pc only : 0.0.0.0  or  127.0.0.1
print("your ip is : "+ip)
print("==========================================")
s.bind((ip,50000))                                 #binds address to the socket we want to open
s.listen(5)
s.settimeout(3*60)                                  # times out after 3 min
while True :
    client_sock_obj , client_sock_address = s.accept()    #waits until there is a connection and accepts it
    rodata = client_sock_obj.recv(1024)
    print(f"{client_sock_address} is sending you this msg : {rodata.decode('utf-8')}")
    print("==========================================")
    msg=str(input("Please input the message you want to send : "))
    if not msg:
        print("server is terminating after 3 min...")
        break
    msg_encoded=msg.encode('utf-8')
    client_sock_obj.send(msg_encoded)
    client_sock_obj.close()
