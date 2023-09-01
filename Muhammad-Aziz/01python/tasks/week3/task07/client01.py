#! /usr/bin/python3

#Create server receive multiple clients and keep alive
import socket

client01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print(ip)
print("================================")
client01.connect((ip,5000))

while True:
    msg = str(input("please enter the message you want to send: "))
    msg_encoded = msg.encode('UTF-8')
    client01.send(msg_encoded)
    print("================================")
    rodata = client01.recv(1024)
    print(f"{ip} >> {rodata.decode('UTF-8')}")
client01.close()