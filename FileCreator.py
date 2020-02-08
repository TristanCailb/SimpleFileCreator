import random
from os import path, mkdir

extensions = ["exe", "iso", "img", "png", "jpg", "mp3", "mp4", "avi", "wav", "ogg"]
titleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
separatorChar = '_'
folderName = "createdFiles"
titleLength = 20
fileCount = 10

def getRandomExt():
    return random.choice(extensions)

def getRandomTitle():
    title = ""
    for i in range(titleLength):
        if i % 4 == 0 and i != 0:
            title += separatorChar
        else:
            title += random.choice(titleChars)
    title += "." + getRandomExt()
    return title

def createFile():
    title = getRandomTitle()
    try:
        print("Creating file " + title)
        with open(folderName + "/" + title, "w") as file:
            file.write(title)
            file.close()
    except:
        print("Failed to create this file: " + title)

if not path.exists(folderName):
    print("Creating the files folder...")
    mkdir(folderName)
for i in range(fileCount):
    createFile()