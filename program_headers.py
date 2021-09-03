# ---| Module imports |-------------------------------------------------------
import pandas as pd
import re

# ---| Specific imports |-----------------------------------------------------
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from typing import Final
from PySide6.QtWidgets import QApplication, QFileDialog
from matplotlib import pyplot as plt
from random import choice

# ---| Data-processing Constants |--------------------------------------------
STOPWORDS: Final[set] = set(stopwords.words('english'))

# ---| Filetype Constants |---------------------------------------------------
EXCEL_FILETYPE: Final[str] = "Excel Spreadsheet (*.xlsx)"
CSV_FILETYPE: Final[str] = "Comma-Separated Values (*.csv)"
PNG_FILETYPE: Final[str] = "Picture (*.png)"
COLORS: Final[list] = ["#bf0039", "#32a852", "#325aa8"] #RGB

