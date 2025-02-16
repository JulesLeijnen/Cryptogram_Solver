import jsonpickle
from classes import DictWord

with open("wordData.json", "r") as file:
    recreated = jsonpickle.decode(file.read())

print(recreated[4].word)
print(recreated[4].length)
print(recreated[4].containing)