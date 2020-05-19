"""
A wrapper class to represent state of an object,
    including x, y, z, theta, and time stamp
"""
class ObjectState:
    def __init__(self, x, y, z = 0, theta = 0, time_stamp = 0):
        self.x = x
        self.y = y
        self.z = z
        self.theta = theta
        self.time_stamp = time_stamp 

    def __repr__(self):
        if self.z == 0 and self.theta == 0 and self.time_stamp == 0:
            return "[" + self.x + ", "  + self.y + "]"
        else: 
            return "[" + self.x + ", "  + self.y + ", " + self.z  + ", " +\
                self.theta  + ", " +  self.time_stamp + "]"

    def __str__(self):
        if self.z == 0 and self.theta == 0 and self.time_stamp == 0:
            return "[" + self.x + ", "  + self.y + "]"
        else: 
            return "[" + self.x + ", "  + self.y + ", " + self.z  + ", " +\
                self.theta  + ", " +  self.time_stamp + "]"
