import time
import socket

for pings in range(10):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    message = b'{ "direction": "forwards", "distance": "10"}'
    addr = ("127.0.0.1", 4444)

    client_socket.connect(addr)
    client_socket.send(message)
    try:
        data = client_socket.recv(1024)
        print(data)
        
    except socket.timeout:
        print('REQUEST TIMED OUT')

    client_socket.close()