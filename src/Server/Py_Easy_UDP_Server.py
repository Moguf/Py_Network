#!/usr/bin/env python3
# UDP Server.

import socket

port = 10600
MAX_SIZE = 65535
target_address = '127.0.0.1'

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((target_address,port))

while True:
    data,address = s.recvfrom(MAX_SIZE)
    text = data.decode('ascii')
    print(text)
