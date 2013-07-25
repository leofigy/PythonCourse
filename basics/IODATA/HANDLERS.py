from subprocess import Popen, PIPE
""" class to execute commands """


class Command(object):
    @staticmethod
    def execute(command="cd"):
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        (std_output, std_error) = process.communicate()
        return_code = process.returncode

        return return_code, std_output, std_error


def loadFile(filename="file.txt", raw=False):
    """ Returns file content ,
        raw : returns a string with all data of the file
        default value: False this returns a list of file values
    """ 
    data = []
    try:
        File2Read = open(filename, "r")
    except:
        print "{0}: Unable to open file".format(__file__)
        return data

    """ If everything was ok , let's continue working """
    if raw:
        data = File2Read.read()
    else:
        data = [line.strip().lower() for line in File2Read]
        # strip removes the tail and head such white spaces, or new lines. 

    """ closing file """
    File2Read.close()
    return data

