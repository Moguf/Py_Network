#!/usr/bin/env python3

import socket

port = 12345
MAX_SIZE = 65535
target_address = '127.0.0.1'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((target_address,port))
s.listen(2)
conn, addr = s.accept()
# conn: socket is the client socket.
print(addr, "Now Connected")
text = "Thank you for connecting from TCP Server."
data = text.encode('ascii')
conn.send(data)
conn.close()

