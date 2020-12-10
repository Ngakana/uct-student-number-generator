# LIBRARIES
import os
import requests
from bs4 import BeautifulSoup

# CONSTANTS AND GLOBAL VARIABLES
NAMES_URL = "https://www.behindthename.com/names/usage/southern-african"
SURNAMES_URL = "https://surnames.behindthename.com/submit/names/usage/southern-african"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"}

NAMES_FILE = "data/names.txt"
SURNAMES_FILE = "data/surnames.txt"

# FUNCTION DEFINITIONS
def scrape_names(url, filepath, save=False):
    names_page_request = requests.get(url, headers=headers)

    if names_page_request.status_code == 200:
        parsed_html = BeautifulSoup(names_page_request.content, "html.parser")
        name_items = parsed_html.find_all("span", attrs={"class":"listname"})
        names = [name.text.title() for name in name_items]

        if save:
            if not os.path.exists(os.path.dirname(filepath)):
                os.makedirs(os.path.dirname(filepath))

            with open(filepath, 'w') as f:
                for name in names:
                    f.write(name)

# MAIN
def main():
    scrape_names(NAMES_URL, NAMES_FILE, True) 
    scrape_names(SURNAMES_URL, SURNAMES_FILE, True)
    
# END OF MAIN

if __name__ == '__main__':
    main()