import socket
import os
import sys

socket_path = "/home/ifiok/school/Final_project/IRobot_Control/ipc/ipc.sock"

try:
    os.unlink(socket_path)
except OSError:
    pass

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.bind(socket_path)

s.listen()

while 1:
    conn, addr = s.accept()
    try:
        while 1:
            data = conn.recv(16)
            if data:
                print("received: ", data)
                conn.send(b'test')
    finally:
        conn.close()