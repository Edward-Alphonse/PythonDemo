from socket import *

class Client:
    _host = '192.168.1.7'
    _port = 21567
    _bufSize = 1024
    _addr = (_host, _port)

    def setup(self):
        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
        self.tcpCliSock.connect(self._addr)

    def read(self):
        data = self.tcpCliSock.recv(self._bufSize)
        return data

    def write(self):
        data = input("> ")
        if not data:
            raise NotImplementedError
        self.tcpCliSock.send(data.encode("UTF-8"))

    def close(self):
        self.tcpCliSock.close()


if __name__ == "__main__":
    client = Client()
    client.setup()
    while True:
        client.write()
        data = client.read()
        if not data:
            break
        print(data) 
    client.close()