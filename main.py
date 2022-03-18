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
    #while True:
        # Movement input
        # direction = input("Please enter direction (options include 'forward', 'backward', 'left', right', 'left180' and 'right180', 'Exit')\n-->")
        
        message, address = server_socket.recvfrom(1024)
        # print(message.decode("utf-8"))

        recv = json.loads(message.decode("utf-8")) #convert byte to string
        print(recv)
        command = recv["command"]
        direction = command["direction"]
        distance = command["distance"]
        print("Direction is: ", direction)
        print("Distance is: ", distance)

        #Movement controls based on input
        if direction == "forwards":

            robot.Drive_forward(distance)
            robot.stop()
        elif direction == "backwards":
            robot.Drive_forward(distance)
            robot.stop()
        elif direction == "left":
            robot.Turn_left(distance)
            robot.stop()
        elif direction == "right":
            robot.Turn_right(distance)
            robot.stop()

        else:
            print("Invalid direction, try again \n")
            # msg = b'Invalid message'
            # server_socket.sendto(msg, address)
    

if __name__ == "__main__":
    main()

