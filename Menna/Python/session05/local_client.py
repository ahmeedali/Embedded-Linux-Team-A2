import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())       #you can use standard ip that indicates your pc only : 0.0.0.0  or  127.0.0.1
print("your ip is : "+ip)
client.connect((ip,50000))                          #you must know the address you want to connect to through : dns (if on the internet) + port (80)
print("==========================================")
client.settimeout(2*60)                             # times out after 2 min
while True:
    msg=str(input("Please input the message you want to send : "))
    if not msg:
        print("client terminated")
        break
    msg_encoded=msg.encode('utf-8')
    client.send(msg_encoded)
    print("==========================================")
    rodata = client.recv(1024)
    print(f"{ip} is sending you this msg : {rodata.decode('utf-8')}")
    print("==========================================")
    #client.close()   #for keeping the client alive ...will terminate from server side
