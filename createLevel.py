from classes import LevelWord, DictWord, Level

def createLevel(wordsArray, inputstring):
    level = Level(initString=inputstring, allKnown=wordsArray)
    level.convertInitString()
    return level