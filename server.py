# import random
import socket
import json

#TCP socket on port 4444
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 4444))
server_socket.listen(1)
# conn, addr = server_socket.accept()

while True:
    conn, addr = server_socket.accept()
    msg = b'{ "result":"success"}'
    message = conn.recv(1024)
    print(message.decode("utf-8"))

    recv = json.loads(message.decode("utf-8")) #convert byte to string
    print(recv["direction"])

    conn.send(msg)
conn.close()