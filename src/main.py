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
    6 - Convert to lower case
    7 - Substitute emails
    8 - Substitute URLs
    9 - Remove Emojis
    10 - Demojize
    11 - Remove HTML Tags
    12 - Translate All Text to original language
    13 - Translate
    14 - Remove Stop Words
    15 - NER
    16 - Lemmatization
    17 - Spellchecking
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
                6 : menuLogic.toLowerCase,
                7 : menuLogic.subEmails,
                8 : menuLogic.subURLs,
                9 : menuLogic.removeEmojis,
                10 : menuLogic.demojize,
                11 : menuLogic.removeHTMLTags,
                12 : menuLogic.translateAllTextToOriginalLanguage,
                13 : menuLogic.translate,
                14 : menuLogic.removeStopWords,
                15 : menuLogic.ner,
                16 : menuLogic.lemmatization,
                17 : menuLogic.spellchecking
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