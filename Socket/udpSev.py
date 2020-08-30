from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_DGRAM)
server.bind(ADDR)
try:
    while True:
        print "Waitting for message"
        data, addr = server.recvfrom(BUFSIZE)
        server.sendto('[%s] %s' %(ctime(), data), addr)
        print('[%s] %s' %(ctime(), data))
finally:
    server.close()