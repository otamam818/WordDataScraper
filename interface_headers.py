import program_main
from typing import Final
from pyperclip import paste
from PySide6.QtWidgets import QApplication, QFileDialog

# ---| Interface Constants |--------------------------------------------------
ASK_NUMBER: Final[str] = "Select a number: "
SEPARATOR:  Final[str] = "-----------------------------------------------------------------------------"

# ---| Feature Constants |----------------------------------------------------
FEATURE_CHOICES: Final[str] = "\n".join([
        "1. Analyze text",
        "2. Make graphical data from .csv or xlsx"
    ]
)

# ---| Text Input constants |-------------------------------------------------
TEXT_INPUT_CHOICES: Final[str] = "\n".join([
        "1. Choose from a file in your system",
        "2. Extract from clipboard",
        "3. Insert manually"
    ]
)

# ---| Text Analysis constants |----------------------------------------------
TEXT_ANALYSIS_CHOICES: Final[str] = "\n".join([
        "1. Make a table",
        "2. Make a bar graph",
        "3. Make a pie chart"
    ]
)
TEXT_ANALYSIS_ACTIONS: Final[dict] = {
    "1" : program_main.make_table,
    "2" : program_main.make_bar_graph,
    "3" : program_main.make_pie_chart
}
