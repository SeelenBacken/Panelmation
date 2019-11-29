class Line:
    def __init__(self, LineNr):
        self.nr = LineNr

class Led:
    def __init__(self, LedNr, x, y, color):
        self.nr = LedNr
        self.y = y
        self.x = x
        self.color = color

class LEDMatrix:

    def setAll(self, color):
        for led in self.Leds:
            led.color = color

    def __init__(self):
        self.Leds = []
        self.Lines = []

        self.maxRow = 25
        self.maxLed = 60

        for y in range(self.maxRow):
            for x in range(self.maxLed):
                self.Leds.append(Led(x*y, x*18+50, y*18+50, (0, 0, 0)))
