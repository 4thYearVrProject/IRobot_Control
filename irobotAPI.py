from  pycreate2 import Create2
import time

class Irobot();
    def __init__(self,portNumber);
        self.port
        self.bot
        self.init = False

def Start(self,portNumber):
        self.port = "/dev/serial" + self.portNumber  # where is your serial port?
        self.bot = Create2(self.portport)
        # Start the Create 2
        self.bot.start()
        self.init = True
        print("Robot started")

def Stop(self):
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

