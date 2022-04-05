import irobotAPI
import sys
import socket
import json

def main():
    #UDP socket on port 4444
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 4444))

    robot = irobotAPI.Irobot("ttyUSB0")
    robot.start()

    
    while robot.init == True:       
        message, address = server_socket.recvfrom(1024)
        # print(message.decode("utf-8"))

        recv = json.loads(message.decode("utf-8")) #convert byte to string
        print(recv)
        command = recv["command"]
        direction = command["direction"]
        distance = command["distance"]

        print("Direction is: ", direction)
        print("Distance is: ", distance)

        #Movement controls based on input can be forwards, backwards, left or right
        if direction == "forwards":
            robot.Drive_forward(distance)
            if distance != 0:
                robot.stop()
        elif direction == "backwards":
            robot.Drive_backward(distance)
            if distance != 0:
                robot.stop()
        elif direction == "left":
            robot.Turn_left(distance)
            if distance != 0:
                robot.stop()
        elif direction == "right":
            robot.Turn_right(distance)
            if distance != 0:
                robot.stop()
        elif direction == 'stop':
            robot.stop()
        else:
            print("Invalid direction, try again \n")
    

if __name__ == "__main__":
    main()

