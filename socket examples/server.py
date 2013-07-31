#!/usr/bin/env python
""" Networking application server side """
from socket import *
import thread
import sys


class Netserver(object):
    def __init__(self, host='', port=5000, clients=5, message='''Hi there !!! I'm python server'''):
        self.socket = socket()
        self.socket.bind((host, port))
        self.socket.listen(clients)  # The number of clients to be queued
        self.message = message

    def clientHandling(self, connection, size=1024):
        data = None
        while True:
            try:
                connection.send(self.message)
            except:
                print "Unable to send information to client"

            try:
                data = connection.recv(size)
            except:
                print "----> User left !!"
                connection.close()
                break
            print data

    def __run__(self):
        # Starting connections
        while True:
            connection, address = self.socket.accept()
            thread.start_new_thread(self.clientHandling, (connection,))
        self.socket.close()


def main():
    print "Welcome to remote server {0}".format(gethostname())  # gethostname is inside socket module
    server = Netserver()
    server.__run__()

if __name__ == '__main__':
    main()
    sys.exit(0)

