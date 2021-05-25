import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5000))
serversocket.listen(1) # become a server socket, maximum 5 connections


while True:
    connection, address = serversocket.accept()
    buf = connection.recv(512)
    if len(buf) > 0:
        print(buf)
        break

print("Socket Ended")

'''
while True:
    time.sleep(5)
    data = serversocket.recv(512)
    if data.lower() == 'q':
        serversocket.close()
        break
    else:
        print("Message Recieved: %s" % data)
        data = input("Type Q to quit! : ")
        serversocket.send(data)
        if data.lower() == 'q':
            serversocket.close()
            break
'''