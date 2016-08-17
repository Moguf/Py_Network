# Py_Network/Server
Fundamental Server API.

## Requirements
- Python3 > 3.5.1

### socket.socket()
```python
socket.socket(socket_family, socket_type,protocol=0)
"""
    socket_family: socket.AF_INET, PP_PACKET
        socket.AF_INET     : IPv4
        socket.PF_PACKET   : Device Driver
    socket_type: socket.SOCK_DGRAM, socket.SOCK_RAW, socket.SOCK_STREAM
        socket.SOCK_DGRAM  : UDP
        socket.SOCK_STREAM : TCP   
        socket.SOCK_RAW    : 
"""
```
### Socket Methods
```python
### Server socket methods
socket.bind(address)          # address = (IP address,port number).
socket.listen(q)              # TCP listener.
socket.accept()               # Before this module, socket.bind(address) socket.listen(q).

### Client socket methods
socket.connect(address)       # address = Server address.

### General socket methods
socket.recv(bufsize)          # Recevies TCP message.
socket.recvfrom(bufsize)      # Recevies data from the socket. return (data, address)
socket.recv_into(buffer)      # buffer is from bytearray().
socket.recvfrom_into(buffer)  # return (nbytes, address)
socket.send(bytes)            # send data to the socket.
socket.sendto(data, address)  # UDP protocol
socket.sendall(data)          # send all data to the socket.
```

## Reference
- https://github.com/brandon-rhodes/fopnp

