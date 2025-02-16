#import
import re
#classes

class DictWord:
    
    def __init__(self, word):
        self.word = word.lower()
        self.length = len(word)
        self.containing = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
        possibleCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for charIndex in range(0, len(possibleCharacters)):
            self.containing[charIndex] = self.word.count(possibleCharacters[charIndex])

class LevelWord:
    
    def __init__(self, length, knowns, allWords):
        self.length = length
        self.word = [0] * length
        for charIndex in range(0, len(knowns)):
            self.word[charIndex] = knowns[charIndex]
        self.possibilities = allWords
        self.possibleCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.regexString = ""
        
    def printWord(self):
        print(self.word)
    
    def printPossibilities(self):
        print(self.possibilities)
    
    def possibilitiesFilterLength(self):
        print(len(self.possibilities))
        self.possibilities = list(filter(lambda x: x.length == self.length, self.possibilities))
        print(len(self.possibilities))
        print("Shortened To Length")

    # def createRegexString(self):
    #     self.regexString = ""
    #     for char in self.word:
    #         print(char)
    #         if char in self.possibleCharacters:
    #             self.regexString = self.regexString + char
    #         else:
    #             self.regexString = self.regexString + "."
    #     print(self.regexString)
    
    def possibilitiesFilterKnowns(self):
        print(len(self.possibilities))
        for letterIndex in range(0, self.length):
            self.possibilities = list(filter(lambda x: self.word[letterIndex] == x.word[letterIndex] or (x.word[letterIndex] not in self.possibleCharacters or self.word[letterIndex] not in self.possibleCharacters), self.possibilities))
            print(len(self.possibilities))
        for x in self.possibilities:
            print(x.word)
class Level:
    
    def __init__(self, initString, allKnown):
        self.initString = initString.lower()
        self.words = []
        self.allKnown = allKnown
    
    def convertInitString(self):
        splitWords = self.initString.split()
        for word in splitWords:
            wordLength = word.count(",") + 1
            characterArray = word.split(",")
            self.words.append(LevelWord(wordLength, characterArray, self.allKnown))