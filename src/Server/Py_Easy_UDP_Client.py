#!/usr/bin/enc python3
# Client

import socket

port = 10600
MAX_SIZE = 65535
target_address = '127.0.0.1'

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
text = 'Hello World!!'
data = text.encode('ascii')
s.sendto(data,(target_address,port))

