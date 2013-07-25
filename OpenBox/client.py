import os
import sys
import hashlib
from optparse import OptionParser

""" Adding process libraries """
import time  # has time utilities
import multiprocessing  # has multiple input

""" Custom Exceptions """


class ClientExceptions(Exception):
    # exceptions for client
    def __init__(self, code, value="Unknown issue"):
        """ overloading first exception """
        error_dict = {
            1: "No channel provided to send data fatal error"
        }
        self.value = error_dict[code]

    def __str__(self):
        return repr(self.value)  # returns the canonical string representation of the object


class client(object):

    def __init__(self,
                 cwd=os.getcwd(),
                 mutex=None):
        self.workingDirectory = cwd
        """ creating current file list """

        """ Lambda functions """
        self.filePath = lambda a, b: os.path.join(a, b)
        self.FileInformation = self.getDictionary()
        self.Temporal = {}
        self.mutex = mutex

    def run(self, queue=None, interval=1):
        if not queue:
            raise ClientExceptions(1)
        """ starting to run function """
        while True:
            """<<<< Here goes your solution >>>>"""
            self.Temporal = self.getDictionary()
            if not self.FileInformation == self.Temporal:
                """ processing operations """
                with self.mutex:
                    print "Generador", len(self.Temporal.keys())

                # sending operation to saver function
                queue.put(True)

            time.sleep(interval)

    def saveData(self, queue=None):
        while True:
            if queue.get():
                with self.mutex:
                    print len(self.FileInformation.keys())

    def getFiles(self):
        """ return the list of current files """
        fileList = []
        root = self.workingDirectory
        fileList = [self.filePath(root, filex) for (root, dirs, files) in os.walk(root) for filex in files]
        return fileList

    def getDictionary(self):
        files = self.getFiles()
        dictionary = {}
        fileAndHashes = []
        if files:
            fileAndHashes = [(filex, self.getChecksum(filex)) for filex in files]
        dictionary = dict(fileAndHashes)
        return dictionary

    def getChecksum(self, filename):
        if not filename:
            return []
        """ using sha256 """
        hasher = hashlib.sha256()
        filex = open(filename, "rb")
        while True:
            byteCode = filex.read(2**20)
            if not byteCode:
                break
            hasher.update(byteCode)
        filex.close()
        return hasher.digest()


def main():
    mutex = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    OpenDrop = client(cwd="/Users/leofigy/repositories/PythonCinvestav/basics", mutex=mutex)
    interval = 1
    """ moving all solutions to multiple processes """

    message = """ ================ Welcome to OpenDrop Client ================= \n \
              Monitoring Folder: {0} :""".format(OpenDrop.workingDirectory)

    """ Preparing all processes """
    scan = multiprocessing.Process(target=OpenDrop.run, args=(queue, interval,))
    saver = multiprocessing.Process(target=OpenDrop.saveData, args=(queue,))
    scan.start()
    saver.start()

    print message
    while True:
        raw_input("Press enter ")
        with mutex:
            out = raw_input("Press q for quit : ")
            if out == 'q':
                scan.terminate()
                saver.terminate()
                return


if '__main__' == __name__:
    main()
    sys.exit(0)


""" NOTES """

""" Python classes format

    notes : self it is the referene to the same instance

    class className(father):

        def __init__(self):
            'this is the constructor'

        def method_name(self, paramters):
            'method function etc ...'

"""
