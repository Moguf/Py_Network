# Py_Network/Server
Fundamental Server API.

## Requirements
- Python3 > 3.5.1

```python
import socket
```

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
socket.listen(q)              # TCP listener. q is the number of acceptable connections.
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

### Socket Exceptions
```python
exception socket.herror       # address-related error.
exception socket.timeout      # 
exception socket.gaierror     # caches any exception from getaddinfo() and getnameinfo()
exception socket.error        # socket-related errors. -> this can catch any type of exception.
```
### Userful socket methods
```python
socket.gethostbyname(name)                    # return IPv4 address format. ex) name = 'google.com'
socket.gethostbyname_ex(name)                 # return all IPv4 address formas og domain name. not work for IPv6. ex) name = 'google.com'
socket.gethostname(name)                      # get host name. (name <-> IPv4)
socket.gethostname_ex(name)                   # get IP address of all the interfaces. (name <-> IPv4)
socket.getfqdn(name)                          # get fully qulified domain name(FQDN).
socket.gethostbyaddr(ip_address)              # get the domain name from IP address.
socket.getservbyname(servicename[,protocol])  # convert any protocol name to port number
socket.getservbyport(port,[protocol])         # return protocol name.
socket.connect_ex(address)                    # Success: return 0. Failure: errno variable.

```


## Reference
- http://docs.python.jp/3/library/socket.html
- https://github.com/brandon-rhodes/fopnp
- [Python Penetration Testing Essentials](https://www.amazon.com/dp/1784398586/)
