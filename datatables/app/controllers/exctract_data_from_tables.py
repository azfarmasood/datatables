from bs4 import BeautifulSoup, Tag 
import pandas as pd
from typing import cast
def extract_table_data(soup: BeautifulSoup, table_id: str) -> pd.DataFrame:
    """Pull data from HTML table and convert to DataFrame"""
    # Find our table
    table = soup.find('table', {'id': table_id})
    if not table:  # More pythonic way to check for None
        raise Exception(f"Couldn't find table with id '{table_id}'!")
    
    table = cast(Tag, table)
    print("Table found successfully")
    
    # Get headers - list comprehension for simple operations
    thead = table.find('thead')
    if not thead:
        headers = []  # No type annotation here - obvious from context
    else:
        headers = [th.text.strip() for th in cast(Tag, thead).find_all('th')]
    
    print(f"Found these headers: {headers}")
    
    # Extract rows - traditional loop here (humans mix approaches)
    rows = []
    tbody = table.find('tbody')
    if tbody:
        tbody = cast(Tag, tbody)
        for tr in tbody.find_all('tr'):
            tr = cast(Tag, tr)
            row = []
            for td in tr.find_all('td'):
                row.append(td.text.strip())
            rows.append(row)
    
    print(f"Found {len(rows)} rows of data")
    
    # Make a DataFrame
    return pd.DataFrame(rows, columns=headers)