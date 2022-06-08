import TextProcessor as TP
from main import clearScreen

global tp
tp = TP.TextProcessor()

INPUT_FOLDER_PATH = "../input/"
OUTPUT_FOLDER_PATH = "../output/"

def insertDataset():
    try:
        choice = int(input("""0 - Input
1 - File
-> """))
        if choice == 0:
            text = input('Insert dataset: ')
        elif choice == 1:
            fileName = input("File Name: ")

            with open(INPUT_FOLDER_PATH + fileName,"r") as f:
                text = f.read()
        else:
            clearScreen()
            print("Please enter a valid choice")
            input("Press enter to continue\n")
            return
             
        tp.insertDataset(text)
        input("Press enter to continue")

    except ValueError:
        clearScreen()
        print("Please enter a valid choice")
        input("Press enter to continue\n")

def printDataset():
    dataset = tp.getDataset()
    clearScreen()
    print(dataset)
    input("\n\n\nPress enter to continue\n")
    clearScreen()

def saveDataset():
    fileName = input("File name: ") + '.txt'
    dataset = tp.getDataset()
    with open(OUTPUT_FOLDER_PATH + fileName,"w") as f:
        f.write(dataset)
        f.flush()

    clearScreen()

def removePonctuation():
    tp.removePonctuation()

def normalizeWhitespaces():
    tp.normalizeWhitespaces()

def toLowerCase():
    tp.toLowerCase()

def subEmails():
    change = input("Sub for (Defaults for \"Email\"): ")
    change = 'Email' if change == '' else change
    tp.subEmails(change)

def subURLs():
    change = input("Sub for (Defaults for \"URL\"): ")
    change = 'URL' if change == '' else change
    tp.subURLs(change)

def removeEmojis():
    tp.removeEmojis()

def demojize():
    tp.demojize()

def removeHTMLTags():
    tp.removeHTMLTags()

def translateAllTextToOriginalLanguage():
    tp.translateAllTextToOriginalLanguage()

def translate():
    tp.translate()

def removeStopWords():
    tp.removeStopWords()

def ner():
    tp.ner()

def lemmatization():
    tp.lemmatization()

def spellchecking():
    tp.spellchecking()