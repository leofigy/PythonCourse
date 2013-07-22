""" 
    Small python application to read an load data from a file  
    Notes: __file__ : returns the name of the current file 
"""
import sys
from optparse import OptionParser 

'Importing from our custom modules (namespaces)'
import IODATA.HANDLERS as readers 


def Parser():
    """ The parser function defines the ser of elements to be processed by
        our application """

    options = None 
    arguments = None

    """ Creating an object parser """ 
    Parser = OptionParser()
    """ Parameters defined to the user 
        1) --file : File to be used to open the dictionary
        2) --word : Word to be search inside dictionary 
    """
    Parser.add_option("-f", "--file", dest="filename",
                  help="Input dictionary", metavar="FILE",
                  default="FILES/countries.txt")

    Parser.add_option("-w", "--word", dest="word",
                  help="Word2Search", metavar="WORD",
                  default="Mexico")

    try:
        (options, arguments) = Parser.parse_args()

    except:
        print "{0} :Unable to handle arguments".format(__file__)

    """ returning tuples """
    return options, arguments 



def main():
    """ Here starts the main function """
    (options, arguments) = Parser()
    print "File: {0}  \n Word: {1}".format(options.filename, options.word)
    
    """ Getting a list with file content """ 
    listFile = readers.loadFile(options.filename)
    stringFile = readers.loadFile(options.filename, raw=True)

    print "CURRENT LIST {0}".format(listFile)
    Word2Search = options.word.lower()
    """ Basic handling """
    while True:
        print "*) Looking for word: {0} \n ".format(Word2Search)
        # Perfect match 
        if Word2Search in listFile:
            print " Word Found !!!"
        else:
            """<<<<<<<<< here goes your solution 
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
            
        print "*) What to exit, press Y:"
        decision = raw_input().lower()
        if decision == 'y':
            print "Thank you !!!"
            break
        """ Introduce new word """
        print "*) Introduce new word : \n"
        Word2Search = raw_input().lower()

    return True

if '__main__' == __name__:
    """ here executes main """
    return_value = main()
    if return_value:
        sys.exit(0)
    sys.exit(1)
