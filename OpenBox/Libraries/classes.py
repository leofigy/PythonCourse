"""
    This module contains the following classes:
        *) ClientException
        *) Client
"""

import os
import sys
import hashlib
from optparse import OptionParser

''' Adding process libraries '''
import time  # has time utilities
import multiprocessing  # has multiple input

''' Custom Exceptions  '''


class ClientExceptions(Exception):
    """ Known exceptions for client app """
    def __init__(self, code, value="Unknown issue"):
        ''' overloading first exception '''
        error_dict = {
            "Queue": "No queue provided to send data fatal error",
            "Arguments": ":( Sorry unable to process your arguments , python client.py help for details",
            "Invalid Arguments": "Please verify the type of your arguments !!"
        }
        self.value = error_dict[code]

    def __str__(self):
        return repr(self.value)  # returns the canonical string representation of the object


class Client(object):
    """ Class client for our application """
    def __init__(self, cwd=os.getcwd(), mutex=None):
        self.working_directory = cwd
        ''' creating current file list '''
        self.current_files = self.getDictionary()
        self.scanned_files = {}
        self.mutex = mutex

    """ Fix for windows : lambda functions are not able to be changed adding """
    def filePath(self, a, b):
        return os.path.join(a, b)

    def run(self, queue=None, interval=1):
        if not queue:
            raise ClientExceptions("Queue")
        ''' starting to run function '''
        while True:
            '''<<<< Here goes your solution >>>>'''
            self.scanned_files = self.getDictionary()
            if not self.current_files == self.scanned_files:
                ''' processing operations '''
                with self.mutex:
                    print "Generador", len(self.scanned_files.keys())

                # sending operation to saver function
                queue.put(True)

            time.sleep(interval)

    def saveData(self, queue=None):
        while True:
            if queue.get():
                with self.mutex:
                    print len(self.current_files.keys())

    def getFiles(self):
        """ return the list of current files """
        fileList = []
        root = self.working_directory
        fileList = [self.filePath(root, filex) for (root, dirs, files) in os.walk(root) for filex in files]
        return fileList

    def getDictionary(self):
        """ returns a dictionary with {"filename": "checksum"} format """
        files = self.getFiles()
        dictionary = {}
        fileAndHashes = []
        if files:
            fileAndHashes = [(filex, self.getChecksum(filex)) for filex in files]
        dictionary = dict(fileAndHashes)
        return dictionary

    def getChecksum(self, filename):
        """ returns the checksum using hashlib """
        if not filename:
            return []
        ''' using sha256 '''
        hasher = hashlib.sha256()
        filex = open(filename, "rb")
        while True:
            byteCode = filex.read(2**20)
            if not byteCode:
                break
            hasher.update(byteCode)
        filex.close()
        return hasher.digest()

