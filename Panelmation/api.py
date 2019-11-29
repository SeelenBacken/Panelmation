import socket
from time import sleep

while True:
    for x in range(254):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 6019))
        s.send('setAll {} {} {}'.format(x, x, x).encode('UTF-8'))
        s.close()
        sleep(0.01)

    """
    line = input('>>')
    if line == 'exit':
        break
    s.send(line.encode('utf-8'))
    s.close()"""
