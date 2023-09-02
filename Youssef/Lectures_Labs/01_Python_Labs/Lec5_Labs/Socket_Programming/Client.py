import socket

Client = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #IPv4 , TCP
ip = socket.gethostbyname(socket.gethostname())
print("Your ip is : "+ip)
Client.connect(("127.0.0.1" , 5000))
print("=============================")

msg = str(input("Please enter the message that you want to send : "))
msg_encoded = msg.encode('UTF-8')
Client.send(msg_encoded)

print("=============================")

rodata = Client.recv(1024)
print(f"{ip} is sending to you this message : {rodata.decode('UTF-8')}")
Client.close()