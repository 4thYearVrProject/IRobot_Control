import irobotAPI
import sys

def main():
    robot = irobotAPI.Irobot("ttyUSB0")
    robot.start()
    
    while robot.init == True:
        # Movement controls
        direction = input("Please enter direction (options include 'forward', 'backward', 'left', right', 'left180' and 'right180', 'Exit')\n-->")
        

        if direction == "forward":
            distance = float(input("Please enter a distance to travel in meters \n-->"))
            robot.Drive_forward(distance)
            robot.stop()
        elif direction == "backward":
            distance = float(input("Please enter a distance to travel in meters \n-->"))
            robot.Drive_backward(distance)
            robot.stop()
        elif direction == "left":
            robot.Turn_left()
            robot.stop()
        elif direction == "right":
            robot.Turn_right()
            robot.stop()
        elif direction == "left180":
            robot.turn_backwards_CW()
            robot.stop()
        elif direction == "right180":
            robot.turn_backwards_CCW()
            robot.stop()
        elif direction == "Exit":
            robot.close()
            sys.exit()
        else:
            print("Invalid direction, try again \n")
    

if __name__ == "__main__":
    main()

