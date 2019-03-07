import random

class Weather :
    def __init__(self, num = random.randint(0, 100)) :
        if num > 98 :
            self.storm = True
        else :
            self.storm = False
