import irobotAPI

def main():
    robot = Irobot()
    robot.start()
    
    while robot.init == True
        # Movement controls
        direction = input("Please enter direction (options include 'forward', 'backward', 'left', right', 'left180' and 'right180')")

        if direction == "forward":
            robot.Drive_forward(1)
        elif direction == "backward":
            robot.Drive_backward(1)
        elif direction == "left":
            robot.Turn_left()
        elif direction == "right":
            robot.Turn_right()
        elif direction == "left180":
            robot.turn_backwards_CW()
        elif direction == "right180":
            robot.turn_backwards_CCW()
        else:
            print("Invalid input, try again")
    
    

if __name__ == "__main__":
    main()

