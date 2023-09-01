#! /usr/bin/python3

#Create server receive multiple clients and keep alive
import socket

client02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print(ip)
print("================================")
client02.connect((ip,5000))

while True:
    msg = str(input("please enter the message you want to send: "))
    msg_encoded = msg.encode('UTF-8')
    client02.send(msg_encoded)
    print("================================")
    rodata = client02.recv(1024)
    print(f"{ip} >> {rodata.decode('UTF-8')}")
client02.close()