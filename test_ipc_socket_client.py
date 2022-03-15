import socket

socket_path = "/home/ifiok/school/4thYearProject/IRobot_Control/ipc/ipc.sock"

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(socket_path)
while 1:
    s.send(b'Hello, world')
    data = s.recv(1024)

    print('Received ' + repr(data))

s.close()