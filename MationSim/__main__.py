import pygame
import sys
import socket
from MationSim import leds


class MationSim:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    LineNr = 25
    LedNr = 60

    def startThread(self, connection):
        while True:
            try:
                if connection:
                    c, addr = connection.accept()
                    received = c.recv(1204).decode('UTF-8').split()
                    if received[0] == 'setAll':
                        print('Incoming: {}'.format(received[0]))
                        self.matrix.setAll((int(received[1]), int(received[2]), int(received[3])))
            except Exception as ex:
                i = 1
            count = -1
            for led in self.matrix.Leds:
                pygame.draw.circle(self.windowSurface, led.color, (led.x, led.y), 6)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    connection.close()
                    pygame.quit()
                    sys.exit()

    def __init__(self):

        RED = (255, 0, 0)

        connection = socket.socket()
        connection.bind(('192.168.0.67', 6019))
        connection.listen(5)
        connection.setblocking(0)

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
        self.startThread(connection)
