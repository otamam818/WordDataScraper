from interface_headers import *

# ---| Main function |--------------------------------------------------------
def main():
    """Where everything starts and ends"""
    print(SEPARATOR)
    choose_input()

# ---| Helper functions |-----------------------------------------------------
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
    choose_tpm(text, qap=True)

def use_pasted(): 
    """Pastes the text currently in the user's clipboard"""
    print(SEPARATOR)
    input("Has your input been copied to clipboard?\nPress ENTER if it has")
    print("copying...")
    text = paste()
    print("Copied!")
    choose_tpm(text)

# ---| Text-processing choice interface |-------------------------------------
def choose_tpm(text, qap=False):
    """
        Choose text processing method
        @param: qap: whether QApplication has been called or not
    """

    # Ask the user what they want to do
    print(SEPARATOR)
    print("What would you like to do with said text:")
    choice = input(TEXT_ANALYSIS_CHOICES + '\n' + ASK_NUMBER)

    # Ask function-specific things and then call the function
    if choice == "1":
        punc, stem = ask_params()
        program_main.make_table(text, punc, qap=qap, to_stem=stem)
    elif choice == "2":
        punc, stem = ask_params()
        top_n = ask_top_n()
        program_main.make_bar_graph(
            text, top_n, qap=qap, 
            punctuation=punc, to_stem=stem
        )

# ---| 'choose_tpm' helper functions |------------------------------------------
def ask_params():
    # Ask user whether they want stemmed words and punctuation
    has_punctuation = input("Inlude punctuation?" + YES_NO) == "1"
    has_stem = ask_stem()
    return has_punctuation, has_stem

def ask_stem() -> bool: 
    print(SEPARATOR + "\nDo you want to join words of the same type?")
    print("For example: Employee and employment will both become employe")
    return input(YES_NO[1:]) == "1"

def ask_top_n() -> int:
    try: 
        num = int(input("Display the values of the top n\n What is n: "))
    except ValueError:
        print("That was not a number; asking again...")
        num = ask_top_n()
    return num

# ---| Python input convention |----------------------------------------------
if __name__ == "__main__":
    main()
