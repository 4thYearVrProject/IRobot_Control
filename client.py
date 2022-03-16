import time
import socket

for pings in range(10):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)

    message = b'{ "direction": "forwards", "distance": "10"}'
    addr = ("127.0.0.1", 4444)

    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        print(data)
        
    except socket.timeout:
        print('REQUEST TIMED OUT')