class Airport:
    def __init__(self):
        self.hanger = []

    def landPlane(self, plane):
        self.hanger.append(plane)

    def takeOffPlane(self, plane):
        self.hanger.pop(self.hanger.index(plane))
