import jsonpickle

def loadWords(jsonWordsDataFile="wordData.json"):
    with open(jsonWordsDataFile, "r") as file:
        dictWords = jsonpickle.decode(file.read())
    return dictWords