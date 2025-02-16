from classes import DictWord
import json
import jsonpickle

file = open("words_alpha.txt", "r")
words = file.read().splitlines()
Dictwords = []
for word in words:
    Dictwords.append(DictWord(word))

jsonStr = jsonpickle.encode(Dictwords)

print(Dictwords[4].containing)

with open("wordData.json", "w", encoding='utf-8') as jsonFile:
    jsonFile.write(jsonStr)