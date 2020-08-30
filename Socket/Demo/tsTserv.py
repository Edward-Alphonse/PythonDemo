from socket import *
from time import ctime

HOST = '192.168.1.8'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSocket = socket(AF_INET, SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)
while True:
    print ("Waitting for connection")
    tcpCliSock, addr = tcpSerSocket.accept()
    print "...connected from:", addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        print data
        if not data:
            break
        str = raw_input("> ")
        tcpCliSock.send('[%s] %s' %(ctime(), str))
    tcpCliSock.close()
tcpSerSocket.close()

