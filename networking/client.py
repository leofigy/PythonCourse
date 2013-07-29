#!/usr/bin/env python
from socket import *
import sys


class NetClient(object):
    def __init__(self, host='', port=1500, size=1024):
        self.socket = socket()
        self.port = port
        self.socket.connect((host, port))  # Tuple to connect to server
        self.size = size

    def __run__(self):
        while True:
            data = self.socket.recv(self.size)
            print data
            message = raw_input("Introduce a message or quit to exit: ")
            if message.lower() == "quit":
                break
            self.socket.send(message)
        self.socket.close()


def main():
    print "Welcome to the client !!!"
    #192.241.130.232
    client = NetClient(host=gethostname())
    client.__run__()


if __name__ == '__main__':
    main()
    sys.exit()


