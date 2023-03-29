import os

# Clears the terminal
def clear():
    os.system('clear')

# Change working directory
def changeDir(path):
    os.chdir(path)

# Create folder in current working directory
def makeDir(dirName):
    os.mkdir(dirName)

# Returns absolute path of current working directory
def currentAbsPath():
    print(os.getcwd())
    return str(os.getcwd())

# Checks if file is empty
def isFileEmpty(file):
    return os.stat(file).st_size == 0