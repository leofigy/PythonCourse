import os  # importing os module
import sys
from IODATA.HANDLERS import Command


def basicInformation():
    return """*) Name: {0} \
              *) Python Version : {1} \
    """.format(sys.platform, sys.version)


def main():
    print """ The os module provides a lot of functions to interact with the OS """
    print basicInformation()
    print "current file: {0}".format(__file__)
    print "current directory: {}".format(os.getcwd())
    instruction = "ls"
    copy = "cp -R"
    if sys.platform == "win32":
        instruction = "dir"
        copy = "xcopy"
    (code, output, error) = Command.execute(command=instruction)
    files = output.splitlines()
    show = lambda x: "*) {0}".format(os.path.abspath(x))
    for fileX in files:
        print show(fileX)

    user_input = raw_input("do you want to generate a copy of the current directory? yes/no : ")
    if user_input.lower() != "yes":
        return
    user_input = raw_input("Introduce a directory please !!: ")

    instruction = "{0} {1} {2}".format(copy, os.getcwd(), user_input)
    print instruction
    (code, output, error) = Command.execute(command=instruction)
    os.chdir(user_input)
    print "current file: {0}".format(__file__)
    print "current directory: {}".format(os.getcwd())
    print os.listdir(os.getcwd())


if __name__ == '__main__':
    main()
    sys.exit(0)


