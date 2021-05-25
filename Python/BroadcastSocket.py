import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 5000))
MESSAGE = "Hello"
clientsocket.send(bytes(MESSAGE, 'UTF-8'))

'''
TCP_IP = '192.168.1.72'
TCP_PORT = 5000
BUFFER_SIZE = 512
MESSAGE = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    MESSAGE = input("Enter Number/Message and Q to quit: ")
    if MESSAGE.lower() == 'q':
        break
    s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
'''