#Imports
from loadWords import loadWords
from createLevel import createLevel

#Main
def main():
    wordsArray = loadWords()
    input("Solver for Cryptogram, press enter to go to the first step and fill in the current level\n")
    inputstring = input("Input the current level. Place a ',' between wach letter and use the corresponding numbers for the unknowns. Locked numbers should be reported with a '*' with the number of required unlocks after it. Like this: '*2'. Ignore periods and other punctionation\n\n")
    level = createLevel(wordsArray, inputstring)
    level.words[0].possibilitiesFilterLength()
    #Solve
    #DisplayAnser(s)
    return
#Standard call
if __name__ == "__main__":
    exitCode = main()
    exit(exitCode)
    