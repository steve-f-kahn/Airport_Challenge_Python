class Plane:
    def __init__(self):
        self.flying = True

    def land(self, airport):
        self.flying = False

    def takeoff(self, airport):
        self.flying = True 
