import socket
import random
from time import sleep


def send(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 6019))
    sock.send(message.encode('UTF-8'))
    sock.close()

def sendReceive(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 6010))
    sock.send(message.encode('UTF-8'))
    result = sock.recv(1204)
    sock.close()
    return result


def animationLoop():
    sleep(1)
    while True:
        for z in range(2):
            r, g, b = 0, 0, 0
            if z == 0:
                r, g, b = 255, 255, 255
            else:
                r, g, b = 80, 0, 0
            for y in range(25):
                for x in range(60):
                    send('setLED {} {} {} {} {}'.format(x, y, r, g, b))


if __name__ == '__main__':
    animationLoop()
