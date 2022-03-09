import irobotAPI

def main():
    robot = irobotAPI.Irobot("ttyUSB0")
    robot.start()
    
    while robot.init == True:
        # Movement controls
        direction = input("Please enter direction (options include 'forward', 'backward', 'left', right', 'left180' and 'right180')\n-->")

        if direction == "forward":
            robot.Drive_forward(1)
            robot.stop()
        elif direction == "backward":
            robot.Drive_backward(1)
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
    

if __name__ == "__main__":
    main()

