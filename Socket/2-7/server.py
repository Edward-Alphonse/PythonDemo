from socket import *
from time import ctime

class Server:
    _host = '192.168.1.7'
    _port = 21567
    _bufsize = 1024
    _addr = (_host, _port)

    def setup(self):
        self.tcpSerSocket = socket(AF_INET, SOCK_STREAM)
        self.tcpSerSocket.bind(self._addr)
        

    def listen(self):
        self.tcpSerSocket.listen(5)
        while True:
            print ("Waitting for connection")
            tcpCliSock, addr = self.tcpSerSocket.accept()
            print ("...connected from:", addr)

            while True:
                data = tcpCliSock.recv(self._bufsize)
                print (data)
                if not data:
                    break
                str = input("> ")
                tcpCliSock.send(str.encode("UTF-8"))
            tcpCliSock.close()
        self.tcpSerSocket.close()


if __name__ == "__main__":
    server = Server()
    server.setup()
    server.listen()