import pygame
import sys
from MationSim.leds import Line as Line
from MationSim.leds import Led as Led

class MationSim:

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    LineNr = 25
    LedNr = 60

    def pixel(self, x, y):
        return

    def __init__(self):
        pygame.init()

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)

        LineNr = 25
        LedNr = 60

        windowSurface = pygame.display.set_mode((1400, 630), 0, 32)
        pygame.display.set_caption('MotionSim')

        basicFont = pygame.font.SysFont(None, 48)

        windowSurface.fill(BLACK)


        Leds = []
        Lines = []

        for x in range(LineNr):
            Lines.append(Line(x))
            for y in range(LedNr):
                Leds.append(Led(y, Lines[x], RED))

        while True:
            for lx in Leds:
                pygame.draw.circle(windowSurface, lx.color, (lx.x, lx.y), 10)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
