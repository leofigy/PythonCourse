import os
import sys
import hashlib
from optparse import OptionParser

""" Python classes format

    notes : self it is the referene to the same instance

    class className(father):

        def __init__(self):
            'this is the constructor'

        def method_name(self, paramters):
            'method function etc ...'

"""


class client(object):

    def __init__(self,
                 cwd=os.getcwd()):
        self.workingDirectory = cwd
        """ creating current file list """

        """ Lambda functions """
        self.filePath = lambda a, b: os.path.join(a, b)
        self.FileInformation = self.getDictionary()

    def run(self):
        print "Starting client Monitoring"
        for key, value in self.FileInformation.items():
            print (key, value)

    def getFiles(self):
        """ return the list of current files """
        fileList = []
        root = self.workingDirectory
        fileList = [self.filePath(root, filex) for (root, dirs, files) in os.walk(root) for filex in files]
        return fileList

    def getDictionary(self):
        files = self.getFiles()
        dictionary = {}
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
    OpenDrop = client("/Users/leofigy/repositories/PythonCinvestav/basics")
    OpenDrop.run()


if '__main__' == __name__:
    main()
    sys.exit(0)

