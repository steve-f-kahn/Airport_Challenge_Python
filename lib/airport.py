from weather import Weather

class Airport:
    def __init__(self, weather = Weather()):
        self.hanger = []
        self.weather = weather

    def landPlane(self, plane):
        if self.weather.storm :
            raise RuntimeError("Too stormy to land")

        self.hanger.append(plane)

    def takeOffPlane(self, plane):
        if self.weather.storm :
            raise RuntimeError("Too stormy to take off")
        self.hanger.pop(self.hanger.index(plane))

    def updateWeather(self, weather = Weather()):
        self.weather = weather
