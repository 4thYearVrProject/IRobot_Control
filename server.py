# import random
import socket
import json

#UDP socket on port 4444
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 4444))
# server_socket.listen(1)
# conn, addr = server_socket.accept()

while True:
    # conn, addr = server_socket.accept()
    # msg = b'{ "result":"success"}'
    message, address = server_socket.recvfrom(1024)
    # print(message.decode("utf-8"))

    recv = json.loads(message.decode("utf-8")) #convert byte to string
    print(recv)
    command = recv["command"]
    direction = command["direction"]
    distance = command["distance"]
    print("Direction is: ", direction)
    print("Distance is: ", distance)


#     conn.send(msg)
# conn.close()