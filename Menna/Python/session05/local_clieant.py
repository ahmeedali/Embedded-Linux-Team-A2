import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())       #you can use standard ip that indicates your pc only : 0.0.0.0  or  127.0.0.1
print("your ip is : "+ip)
client.connect((ip,12345))                          #you must know the address you want to connect to through : dns (if on the internet) + port (80)
print("==========================================")
client.settimeout(2*60)                             # times out after 2 min
msg=str(input("Please input the message you want to send : "))
#while True:
#    if not msg:
#        print("client terminated")
#        break
msg_encoded=msg.encode('utf-8')
client.send(msg_encoded)
print("==========================================")
rodata = client.recv(1024)
print(f"{ip} is sending you this msg : {rodata.decode('utf-8')}")
print("==========================================")   
#msg="I got your message.."
#msg_encoded=msg.encode('utf-8')
#client.send(msg_encoded)
print("client closed from client..")  
print("==========================================")  
client.close()
