#import
from copy import deepcopy
#classes

class DictWord:
    
    def __init__(self, word):
        self.string = word
        self.length = len(word)
        self.containing = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
        possibleCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for charIndex in range(0, len(possibleCharacters)):
            self.containing[charIndex] = self.word.count(possibleCharacters[charIndex])

class LevelWord:
    
    def __init__(self, length, knowns, allwords):
        self.length = length
        self.word = [0] * length
        for charIndex in range(0, len(knowns)):
            self.word[charIndex] == knowns[charIndex]
        self.possabilities = allwords
    
    def printWord(self):
        print(self.word)
    
    def printPossibilities(self):
        print(self.possabilities)
    
    def possibilitiesFilterLength(self):
        print(len(self.possabilities))
        self.possabilities = list(filter(lambda x: x.length == self.length, self.possabilities))
        print(len(self.possabilities))
        for x in self.possabilities:
            print(x.string)

class Level:
    
    def __init__(self, initString, allKnown):
        self.initString = initString
        self.words = []
        self.allKnown = allKnown
    
    def convertInitString(self):
        splitWords = self.initString.split()
        for word in splitWords:
            wordLength = word.count(",") + 1
            characterArray = word.split(",")
            self.words.append(LevelWord(wordLength, characterArray, self.allKnown))