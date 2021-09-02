from interface_headers import *

# ---| Main function |--------------------------------------------------------
def main():
    """Where everything starts and ends"""
    FEATURE_ACTIONS = {"1": choose_input}
    print(SEPARATOR)
    choice = ask()
    FEATURE_ACTIONS[choice]()

# ---| Helper functions |-----------------------------------------------------
def ask():
    """Ask the user what they want to do"""
    print(SEPARATOR + "\nWhat do you want to do:")
    print(FEATURE_CHOICES)
    try:
        choice = input(ASK_NUMBER)
        assert(choice.isdigit())
    except:
        print("That was not a number.")
        choice = ask()
    return choice

def choose_input():
    """
        Asks the user how should they insert 
        the text they are interested in
    """
    TEXT_INPUT_ACTIONS = {
        "1" : get_file,
        "2" : use_pasted,
        "3" : get_text
    }
    print(SEPARATOR)
    print("How would you like to enter your file:\n"+TEXT_INPUT_CHOICES)
    choice = input(ASK_NUMBER)
    TEXT_INPUT_ACTIONS[choice]()
    
# ---| Functions related to various text inputs |-----------------------------
def get_text():
    """
        If the user wishes to manually paste the input, 
        they can use this function
    """
    text = ""
    print(SEPARATOR)
    print("Paste your text here. Once you are done, press CTRL+C")
    try:
        while True:
            text += input()
    except KeyboardInterrupt:
        choose_tpm(text)

def get_file(): 
    """Prompts an open file dialog to receive a text file"""
    QApplication([])
    filePath = QFileDialog().getOpenFileName(None, 
        "Choose File:", "", "*.txt")[0]
    with open(filePath, 'r') as myFile:
        text = myFile.read()
    choose_tpm(text)

def use_pasted(): 
    """Pastes the text currently in the user's clipboard"""
    print(SEPARATOR)
    input("Has your input been copied to clipboard?\nPress ENTER if it has")
    print("copying...")
    text = paste()
    print("Copied!")
    choose_tpm(text)

# ---| Text-processing choice interface |-------------------------------------
def choose_tpm(text):
    """Choose text processing method"""
    print(SEPARATOR)
    print("What would you like to do with said text:")
    choice = input(TEXT_ANALYSIS_CHOICES + '\n' + ASK_NUMBER)
    TEXT_ANALYSIS_ACTIONS[choice](text)

if __name__ == "__main__":
    main()
