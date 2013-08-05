#!/usr/bin/env python
from socket import *
import sys


class NetClient(object):
    def __init__(self, host='', port=5000, size=64):
        self.socket = socket()
        self.port = port
        self.socket.connect((host, port))  # Tuple to connect to server
        self.size = size

    def __run__(self):
            
        message = raw_input("Introduce a message or quit to exit: ")
        try:
            self.socket.send(message)
        except :
            print "Unable to send information"
        size =0
        
        while True:
            try:
                data = self.socket.recv(self.size)
            except:
                print "confirmation missed"
                break
            size+=len(data)
            if len(data)==0:break
            else:
                print "server: {0}".format(data)


        self.socket.close()


def main():
    print "Welcome to the client !!!"
    #192.241.130.232
    client = NetClient('')
    client.__run__()


if __name__ == '__main__':
    main()
    sys.exit()


