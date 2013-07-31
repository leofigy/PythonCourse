"""
    Multiprocessing module helps to execute multiple actions within multiple processes
"""
import multiprocessing
from subprocess import Popen, PIPE
import sys
import time

""" This is repeated from other module """


class Command(object):
    @staticmethod
    def execute(command="cd"):
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        (std_output, std_error) = process.communicate()
        return_code = process.returncode

        return return_code, std_output, std_error


def command_execute(command="ls", queue=None, interval=1):
    if not queue:
        return None

    while True:
        (code, std, error) = Command.execute(command)
        queue.put([code, std, error])
        time.sleep(interval)


def Handler(queue=None, interval=3):
    if not queue:
        return None

    while True:
        [code, std, error] = queue.get()
        print "####### Current Files: \n {0} \n ##########code :{1}".format(std, code)
        time.sleep(interval)


def multi(param):
    if param > 2:
        return True
    return False


def main():
    """ communication """
    queue = multiprocessing.Queue()

    print "Single Process"
    sender = multiprocessing.Process(target=command_execute,
                                     args=("ls", queue, 1,))
    receiver = multiprocessing.Process(target=Handler,
                                       args=(queue, 1,))
    sender.start()
    receiver.start()
    sender.join()
    receiver.join()

    '''
    print "Welcome to multiprocess Pool of processes"
    numberOfProcesses = raw_input("Please introduce a number: ")
    try:
        numberOfProcesses = int(numberOfProcesses)
    except Exception:
        numberOfProcesses = 3
        print "Not a number using default value"

    print "Creating pool of processes"
    Pool = multiprocessing.Pool(numberOfProcesses)
    print "Executing "
    print Pool.map(multi, range(numberOfProcesses))
    '''

if __name__ == '__main__':
    main()
    sys.exit(0)
