"""
DataTables Scraper - A tool for extracting and analyzing employee data from DataTables examples
"""

__version__ = "1.0.0"
__author__ = "Afnan and Azfar"
__description__ = "A Python tool that scrapes and analyzes employee data from DataTables demo pages"

# Make key components easily accessible when importing the package
from .app.controllers.scrap_tables_data import fetch_webpage
from .app.controllers.exctract_data_from_tables import extract_table_data
from .app.controllers.cleaning_data import clean_data
from .app.controllers.data_analysis import analyze_data
from .app.controllers.save_to_csv import save_to_csv
from .app.models.analyse_data_models import AnalysisResults

# Expose main function
from .app.main import main

__all__ = [
    'fetch_webpage',
    'extract_table_data',
    'clean_data',
    'analyze_data',
    'save_to_csv',
    'main'
]
