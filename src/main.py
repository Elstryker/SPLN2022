import menuLogic
import os

class Main():

    def __init__(self):
        self.hasInput = False

    def showInputlessMenu(self):
        print("""
    0 - Exit
    1 - Insert dataset
    """)

    def showMenu(self):
        print("""
    0 - Exit
    1 - Insert dataset
    2 - Print dataset on the screen
    3 - Save dataset as a file
    4 - Remove Ponctuation
    5 - Normalize Whitespaces
    6 - Convert to ASCII (Uniformize characters)
    7 - Convert to lower case
    8 - Substitute emails
    9 - Substitute URLs
    10 - Remove Emojis
    11 - Demojize
    12 - Remove HTML Tags
    13 - Translate All Text to original language
    14 - Translate To English
    15 - Remove Stop Words
    16 - NER
    17 - Lemmatization
    18 - Spellchecking
    """)



    def handleInput(self,choice):

        if self.hasInput:
            actions = {
                0 : self.bye,
                1 : menuLogic.insertDataset,
                2 : menuLogic.printDataset,
                3 : menuLogic.saveDataset,
                4 : menuLogic.removePonctuation,
                5 : menuLogic.normalizeWhitespaces,
                6 : menuLogic.convertToASCII,
                7 : menuLogic.toLowerCase,
                8 : menuLogic.subEmails,
                9 : menuLogic.subURLs,
                10 : menuLogic.removeEmojis,
                11 : menuLogic.demojize,
                12 : menuLogic.removeHTMLTags,
                13 : menuLogic.translateAllTextToOriginalLanguage,
                14 : menuLogic.translateToEnglish,
                15 : menuLogic.removeStopWords,
                16 : menuLogic.ner,
                17 : menuLogic.lemmatization,
                18 : menuLogic.spellchecking
            }
        
        else:
            actions = {
                0 : self.bye,
                1 : menuLogic.insertDataset
            }

        toDo = actions.get(choice,self.noSuchCommand)
        toDo()
        
    def bye(self):
        print("Goodbye!")

    def noSuchCommand(self):
        clearScreen()
        print("Please enter a valid choice")
        input("Press enter to continue\n")

    def menu(self):
        print("Welcome to the app")
        choice = -1
        while choice != 0:
            if self.hasInput:
                self.showMenu()
            else:
                self.showInputlessMenu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.hasInput = True
                self.handleInput(choice)
                clearScreen()
            except ValueError as e:
                clearScreen()
                print("Please enter a valid choice")
                input("Press enter to continue\n")
                clearScreen()

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
            


if __name__ == "__main__":
    clearScreen()
    main = Main()
    main.menu()