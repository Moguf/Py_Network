#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Server_ip = '127.0.0.1'
port = 12345
s.connect((Server_ip,port))
print(s.recv(1024))
text = "Hello Server"
data = text.encode('ascii')
s.send(data)
s.close()

