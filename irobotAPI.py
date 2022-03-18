from  pycreate2 import Create2
import time

from sqlalchemy import false

class Irobot():
    #Initialize the robot
    def __init__(self,portNumber):
        self.port = 0
        self.bot = 0
        self.init = False
        self.portNumber = portNumber

    #Start the robot
    def start(self):
        self.port = "/dev/" + self.portNumber  # where is your serial port?
        self.bot = Create2(self.port)
        # Start the Create 2
        self.bot.start()
        self.bot.full()
        self.init = True
        print("Robot started")

    #Stop the robot
    def stop(self):
        if(self.init):
            self.bot.drive_stop()
    
    #Close the robot
    def close(self):
        if(self.init):
            self.init = false
            print("Robot is now off")


    #Drive forward by a specified distance
    def Drive_forward(self, distance):
        if(self.init):
            self.bot.drive_direct(100,100)
            #For motor speed of 100, 100 -> 100 mm/s = 10 cm/s
            # time.sleep(distance/0.1) # Distance is in meters, time = distance / speed
            time.sleep(distance/10)

    #Drive backward by a specified distance
    def Drive_backward(self, distance):
        if(self.init):
            self.bot.drive_direct(-100,-100)
            #For motor speed of -100 -100 -> 100 mm/s = 10 cm/s
            # time.sleep(distance/0.1) # distance is in meters, time = distance / speed
            time.sleep(distance/10)

    #Turn left by specific degrees (CW)   
    def Turn_left(self, angle):
        if(self.init):
            self.bot.drive_direct(100, -100)
            time.sleep(angle/51)

    #Turn right by specific degrees degrees (CCW)    
    def Turn_right(self, angle):
        if(self.init):
            self.bot.drive_direct(-100,100)
            time.sleep(angle/51)
