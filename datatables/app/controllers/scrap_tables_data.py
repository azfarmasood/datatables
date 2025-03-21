from bs4 import BeautifulSoup
import requests
def fetch_webpage(url):
    """Gets webpage HTML content"""
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")
    
    return BeautifulSoup(response.text, 'html.parser')