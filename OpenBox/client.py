import os
import sys
from optparse import OptionParser
from Libraries.classes import Client, ClientExceptions
''' Adding process libraries '''
import multiprocessing  # has multiple input


def getParse():
    options = {}
    arguments = []
    parser = OptionParser()
    parser.add_option("-d", "--directory", metavar="DIRECTORY",
                      default=os.getcwd(), help="Directory to monitor!!", dest="directory")
    parser.add_option("-t", "--interval", metavar="INTERVAL",
                      default=1, help="Time interval to scan the working directory", dest="interval")
    try:
        (options, argumets) = parser.parse_args()
        options.interval = int(options.interval)

    except:
        print "Unable to handle arguments !!!"
        raise ClientException("Arguments")
    return options, arguments


def validateArguments(directory, interval):
    """ validates arguments types and if directory exists """
    if not (isinstance(directory, str) and isinstance(interval, int)):
        print "Instance of different types"
        return False
    if not os.path.exists(directory):
        print "No directory Found"
        return False
    return True


def main():
    """ Client Application for a folder monitor """
    ''' Parsing arguments from command line , there are two arguments
        a) directory : must be a directory like example c:\\
        b) interval : the interval must be the number of seconds

        example:
            python client.py --directory="C:\Users\UserName\OpenDrop" --interval=2
    '''
    (options, arguments) = getParse()

    if not validateArguments(options.directory, options.interval):
        raise ClientException("Invalid Arguments")

    ''' Creating multiprocess elements '''
    mutex = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    OpenDrop = Client(cwd=options.directory, mutex=mutex)
    interval = 1
    ''' moving all solutions to multiple processes '''

    message = """ ================ Welcome to OpenDrop Client ================= \n \
              Monitoring Folder: {0} :""".format(OpenDrop.working_directory)

    ''' Preparing all processes '''
    scan = multiprocessing.Process(target=OpenDrop.run, args=(queue, options.interval,))
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
