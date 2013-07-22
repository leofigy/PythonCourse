import sys

def main():
    """ lambda foo """
    show = lambda a, b:"{0} {1} ".format(a,b)

    print """Python has three basic data structures which are: 
                1) tuples symbol : ()
                2) lists  symbol : []
                3) dicts  symbol : {}
           """

    MyTuple = (1,2,3,4,5,6,7,8)
    print show(type(MyTuple), MyTuple)
    """ A tuple can be thought as a constant list,
    so this means that you cannot change its values """

    MyList = [1,2,3,4,5,6,7,8,9]
    """ A list is the basic unit in python it is a data structure, where one que append or 
    removes elements , and can store any data type """
    print show(type(MyList), MyList)

    MyDict = {"Name": "Angel", "Age": 24, "Country": "Mexico"}
    """ Dictionaries also known has hashes in other languages, are associative arrays, 
    this means to access an element you must now the "key, value" pair """
    print show(type(MyDict), MyDict)

    print """ \n Data structures can contain another data structures 
            List with tuples , dictionaries or other lists."""

    print show(type([]),[MyTuple, MyList, MyDict])
    print show(type(()), (MyTuple, MyList, MyDict))
    print show(type({}),{"tuple": MyTuple, "list": MyList, "dict": MyDict})

    print """ Conversions , one can use the constructor notation list(), dict(), tuple()) \n """
    """ generating a list of tuples """ 

    A = list("hola") 
    B = range(4) # range returns a list of k elements
    AB = zip(A,B) # merge both, to the equal legth, if one is bigger then it cuts until the same length
    """ we can modify this type of list of tupples generating another like this """
    new_list = [(a+a, b+b) for a, b in AB]
    print show(type(new_list), new_list)
    print "\n but as you can see , we can create dictionaries from a list of tuples"
    new_dict = dict(new_list)
    print show(type(new_dict), new_dict)

    """ OPERATORS """

    print """ Data flow and Control structures 
            in:
            Means belong operator, so if an element is contained will return true """
    letter = "a"
    word = "hola mundo"
    print "*) {0} in {1} : {2}".format(letter, word, letter in word)
    print "*) {0} not in {1} : {2}".format(letter, word, letter not in word)


    print "and:", set(range(32)).intersection(set(range(4)))
    print "or", set("hola").union(set("hola mundo"))
    

if __name__ == '__main__':
    main()
    sys.exit(0)