from  pycreate2 import Create2
import time

class Irobot():
    def __init__(self,portNumber):
        self.port = 0
        self.bot = 0
        self.init = False
        self.portNumber = portNumber

    def start(self):
        self.port = "/dev/" + self.portNumber  # where is your serial port?
        self.bot = Create2(self.port)
        # Start the Create 2
        self.bot.start()
        self.bot.full()
        self.init = True
        print("Robot started")

    def stop(self):
        if(self.init):
            self.bot.drive_stop()

    def turn_backwards_CW(self):
        if(self.init):
            self.bot.drive_direct(-360,360)  
            time.sleep(1)


    def turn_backwards_CCW(self):
        if(self.init):
            self.bot.drive_direct(360,-360)  
            time.sleep(1)

    #Drive forward by a specified distance
    def Drive_forward(self, distance):
        if(self.init):
            self.bot.drive_direct(100,100)
            #if 1s = 0.5 m, then t = 2*d
            time.sleep(distance*2) # modify 2 later

    #Drive backward by a specified distance
    def Drive_backward(self, distance):
        if(self.init):
            self.bot.drive_direct(-100,-100)
            #if 1s = 0.5m, then t = 2*d
            time.sleep(distance*2)

    #Turn left 90 degrees (CW)   
    def Turn_left(self):
        if(self.init):
            self.bot.drive_direct(180,-180)
            time.sleep(1)

    #Turn right 90 degrees (CCW)    
    def Turn_right(self):
        if(self.init):
            self.bot.drive_direct(-180,180)
            time.sleep(1)
