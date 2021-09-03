# ---| Module imports |-------------------------------------------------------
import sys, program_main

# ---| Specific imports |-----------------------------------------------------
from typing import Final
from pyperclip import paste
from PySide6.QtWidgets import QApplication, QFileDialog

# ---| Interface Constants |--------------------------------------------------
ASK_NUMBER: Final[str] = "Select a number: "
SEPARATOR:  Final[str] = "-----------------------------------------------------------------------------"
YES_NO: Final[str] = "\n1. Yes\n2. No\nEnter choice: " 

# ---| Choice-based constants |-------------------------------------------------
TEXT_INPUT_CHOICES: Final[str] = "\n".join([
        "1. Choose from a file in your system",
        "2. Extract from clipboard",
        "3. Insert manually"
    ]
)
TEXT_ANALYSIS_CHOICES: Final[str] = "\n".join([
        "1. Make a table",
        "2. Make a bar graph"
    ]
)
