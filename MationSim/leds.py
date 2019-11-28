class Line:
    def __init__(self, LineNr):
        self.nr = LineNr
        print(self.nr)

class Led:
    def __init__(self, LedNr, line, color):
        self.nr = LedNr
        self.line = line
        self.y = self.line.nr*22+50
        self.x = self.nr*22+50
        self.color = color
        print(self.nr)
