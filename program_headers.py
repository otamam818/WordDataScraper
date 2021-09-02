# ---| Module imports |-------------------------------------------------------
import pandas as pd
import re

# ---| Specific imports |-----------------------------------------------------
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from typing import Final
from PySide6.QtWidgets import QApplication, QFileDialog

# ---| Data-processing Constants |--------------------------------------------
STOPWORDS: Final[set] = set(stopwords.words('english'))

# ---| Filetype Constants |---------------------------------------------------
EXCEL_FILETYPE: Final[str] = "Excel Spreadsheet (*.xlsx)"
CSV_FILETYPE: Final[str] = "Comma-Separated Values (*.csv)"

