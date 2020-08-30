from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

client = socket(AF_INET, SOCK_DGRAM)
try:
    while True:
        data = raw_input('> ')
        if not data:
            break
        client.sendto(data, ADDR)
        data, addr = client.recvfrom(BUFSIZE)
        if not data:
            break
        print("data")
finally:
    client.close()