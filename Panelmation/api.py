import socket
from time import sleep

while True:
    line = input('>> ')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 6019))
    s.send(line.encode('UTF-8'))
    s.close()
    sleep(0.005)

    """
    line = input('>>')
    if line == 'exit':
        break
    s.send(line.encode('utf-8'))
    s.close()"""
