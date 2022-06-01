import menuLogic
import os

def showMenu():
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
""")

def handleInput(choice):
    actions = {
        0 : bye,
        1 : menuLogic.insertDataset,
        2 : menuLogic.printDataset,
        3 : menuLogic.saveDataset,
        4 : menuLogic.removePonctuation,
        5 : menuLogic.normalizeWhitespaces,
        6 : menuLogic.toLowerCase,
        7 : menuLogic.subEmails,
        8 : menuLogic.subURLs
    }

    toDo = actions.get(choice,noSuchCommand)
    toDo()
    
def bye():
    print("Goodbye!")

def noSuchCommand():
    clearScreen()
    print("Please enter a valid choice")
    input("Press enter to continue")

def menu():
    print("Welcome to the app")
    choice = -1
    while choice != 0:
        showMenu()
        try:
            choice = int(input("Enter your choice: "))
            handleInput(choice)
            clearScreen()
        except ValueError:
            clearScreen()
            print("Please enter a valid choice")
            input("Press enter to continue")
            clearScreen()

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
            


if __name__ == "__main__":
    clearScreen()
    menu()