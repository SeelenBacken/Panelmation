class Line:
    def __init__(self, LineNr):
        self.nr = LineNr

class Led:
    def __init__(self, LedNr, line, color):
        self.nr = LedNr
        self.line = line
        self.y = self.line.nr*18+50
        self.x = self.nr*18+50
        self.color = color

class hLine:
    hLines = None
    
    def sethLines(self, hLineList):
        hLine.hLines = hLineList
        
    def setColor(self, color):
        for led in self.Leds:
            led.color = color
    
    def __init__(self, LineNr, Leds):
        self.Leds = Leds
        self.nr = LineNr
        self.color = None