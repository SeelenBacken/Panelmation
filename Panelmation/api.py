import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6018))
s.send(b'012')
print('Connected')
s.close()