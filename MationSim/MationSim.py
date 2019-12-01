import pygame
import sys
from MationSim import leds
import threading
import websockets
import asyncio


class MationSim:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    LineNr = 25
    LedNr = 60

    def startThread(self):
        while True:
            count = -1
            for led in self.matrix.Leds:
                pygame.draw.circle(self.windowSurface, led.color, (led.x, led.y), 6)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    async def on_message(self, ws, path):
        async for text in ws:
            textArr = text.split()
            if textArr[0] == 'setLED':
                for x in range(int(textArr[1])):
                    self.matrix.setLED(int(textArr[x*5+2]), int(textArr[x*5+3]), (int(textArr[x*5+4]), int(textArr[x*5+5]), int(textArr[x*5+6])))

    def __init__(self):

        RED = (255, 0, 0)

        self.matrix = leds.LEDMatrix()

        pygame.init()

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)

        self.windowSurface = pygame.display.set_mode((self.LedNr * 18 + 100, self.LineNr * 18 + 100), 0, 32)
        pygame.display.set_caption('MotionSim')

        basicFont = pygame.font.SysFont(None, 48)

        self.windowSurface.fill((47, 55, 55))

        mainThread = threading.Thread(target=self.startThread)
        mainThread.start()

        ws = websockets.serve(self.on_message, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(ws)

        wst = threading.Thread(target=asyncio.get_event_loop().run_forever())
        wst.start()
