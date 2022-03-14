import irobotAPI
import sys

from flask import Flask, request
import json

#app is for listening locally for JSON objects
app = Flask(__name__)

@app.route('/move', methods = ['POST'])
def movement():
    data = request.get_json()
    print(data)
    return json.dumps({"result":"OK"})

def main():
    robot = irobotAPI.Irobot("ttyUSB0")
    robot.start()
    #app.run(port=5000) #To listen on port 5000
    
    while robot.init == True:
        app.run(port=5000)
        # Movement input
        direction = input("Please enter direction (options include 'forward', 'backward', 'left', right', 'left180' and 'right180', 'Exit')\n-->")
        
        #Movement controls based on input
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

