import pygame
import sys
from MationSim.leds import Line as Line
from MationSim.leds import Led as Led
from MationSim.leds import hLine as hLine
from threading import Thread
from multiprocessing import Process

class MationSim:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    LineNr = 25
    LedNr = 60

    def setPixel(self, x, y, color):
        self.Leds[y][x].color = color
        print(self.Leds[y][x].color)
        
    def start(self):
        self.q.start()
        self.p.start()
        
    def startThread(self):
        while True:
            count = -1
            for lineNr in self.Leds:
                count += 1
                for ledNr in self.Leds[count]:
                    pygame.draw.circle(self.windowSurface, ledNr.color,\
                                       (ledNr.x, ledNr.y), 6)
            #for lx in Leds:
             #   pygame.draw.circle(windowSurface, lx.color, (lx.x, lx.y), 6)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
    def sThread(self):
        count = 0
        while True:
            print(count)
            count += 1
            if count >= 10000:
                break

    def __init__(self):
        self.Leds = []
        self.Lines = []
        
        self.LineNr = 25
        self.LedNr = 60
        
        RED = (255, 0, 0)
        
        for x in range(self.LineNr):
            temp = []
            tempLine = Line(x)
            self.Lines.append(tempLine)
            for y in range(self.LedNr):
                temp.append(Led(y, tempLine, RED))
            self.Leds.append(temp)
            
        count=-1
        self.hLines = []
        for x in range(self.LineNr):
            temp = []
            count += 1
            for y in self.Leds[count]:
                temp.append(y)
            tempLine = hLine(count, temp)
            self.hLines.append(tempLine)
        
        hLine.hLines = self.hLines
        pygame.init()

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)

        self.windowSurface = pygame.display.set_mode((self.LedNr*18+100, self.LineNr*18+100), 0, 32)
        pygame.display.set_caption('MotionSim')

        basicFont = pygame.font.SysFont(None, 48)

        self.windowSurface.fill(BLACK)
        self.hLines[2].setColor(GREEN)
        
        self.p = Process(target=self.sThread())
        self.q = Process(target=self.startThread())
        

