
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

#Turn left 90 degrees    
def Turn_left(self, distance):
    if(self.init):
        self.bot.drive_direct(180,-180)
        time.sleep(1)

#Turn right 90 degrees    
def Turn_right(self, distance):
    if(self.init):
        self.bot.drive_direct(-180,180)
        time.sleep(1)
