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
        # Movement input
        # direction = input("Please enter direction (options include 'forward', 'backward', 'left', right', 'left180' and 'right180', 'Exit')\n-->")
        
        message, address = server_socket.recvfrom(1024)
        recv = json.loads(message.decode("utf-8")) #convert byte to string
        direction = recv["direction"]

        #Movement controls based on input
        if direction == "forward":
            # distance = float(input("Please enter a distance to travel in meters \n-->"))
            distance = recv["distance"]
            robot.Drive_forward(distance)
            robot.stop()
        elif direction == "backward":
            # distance = float(input("Please enter a distance to travel in meters \n-->"))
            distance = recv["distance"]
            robot.Drive_forward(distance)
            robot.stop()
        elif direction == "left":
            distance = recv["distance"]
            robot.Turn_left(distance)
            robot.stop()
        elif direction == "right":
            distance = recv["distance"]
            robot.Turn_right(distance)
            robot.stop()
        # elif direction == "left180":
        #     robot.turn_backwards_CW()
        #     robot.stop()
        # elif direction == "right180":
        #     robot.turn_backwards_CCW()
        #     robot.stop()
        # elif direction == "Exit":
        #     robot.close()
        #     sys.exit()
        else:
            # print("Invalid direction, try again \n")
            msg = b'Invalid message'
            server_socket.sendto(msg, address)
    

if __name__ == "__main__":
    main()

