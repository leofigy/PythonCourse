from collections import defaultdict

""" This function has different operations """

def countLetters(word=""):
    """ returns a dictionary with the number of letters 
        that the word has """
    DictionaryWord = {}
    DictionaryWord = defaultdict(lambda:0, DictionaryWord)
    if word:
        for letter in word:
            DictionaryWord[letter]+=1

    return DictionaryWord

    
def decisionFoo(dictA={}, dictB={}):
    if dictA.keys() == dictB.keys():
        return True
    return False

    
def searchSimilarWords(word="", List=[], foo=decisionFoo):
    print "{0}: \n Adding names with the same letters".format(__file__)

    output = []
    if word and List:
        dictWord = countLetters(word)
        output = [word2compare for word2compare in List if foo(dictWord, countLetters(word2compare))]
    return output
    
         

