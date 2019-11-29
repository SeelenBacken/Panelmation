import socket

s = socket.socket()
s.bind(('localhost', 6008))
s.listen(5)

while True:
    c, addr = s.accept()
    c.send('Thank you for connecting'.encode('utf-8'))
    c.close()