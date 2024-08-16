""" 
    Resources:
    - https://www.zippia.com/advice/average-cost-of-groceries-by-state/
"""
import datetime
import os
from typing import List

import pandas as pd
import requests
from bs4 import BeautifulSoup, ResultSet, Tag

RTDIR = os.path.dirname(__file__)

def scrape_website(url: str) -> BeautifulSoup:
    """ Scrape the html document from the website

    Args:
        url (str): The URL to scrape the link from

    Returns:
        BeautifulSoup: A parsed and objectified version of the html document from the link.
    """
    # Perform the request
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers, timeout=10)

    # Check if the HTTP request was successful
    assert response.status_code == 200

    return BeautifulSoup(response.text, 'html.parser')

    print('Failed to retrieve HTML.')
    return None

def parse_html(soup: BeautifulSoup) -> pd.DataFrame:
    """ Extracts useful information from the parsed HTML.

    Args:
        html (BeautifulSoup): HTML file that has been received and parsed by BeautifulSoup

    Returns:
        pd.DataFrame: DataFrame that was constructed and formatted from html data
    """
    # Find all links that contain an href
    links = soup.find_all('script')
    # print(links)

    # For each link, check whether it contains a Wordle option
    option_list = []
    link: Tag
    for link in links:
        if '\"ingredients\"' in link.text:
            # print(f'{i}) {link}')
            # if "/unscramble/" in link['href']:
            option_list.append(link.text.lower())
        # option_list.append(link.text)

    options = pd.DataFrame(option_list)
    return options[0]

def parse_html2(soup: BeautifulSoup, tag: str) -> pd.DataFrame:
    """ Extracts useful information from the parsed HTML.

    Args:
        html (BeautifulSoup): HTML file that has been received and parsed by BeautifulSoup

    Returns:
        pd.DataFrame: DataFrame that was constructed and formatted from html data
    """
    ingredients = pd.DataFrame(columns=['Amount', 'Unit', 'Name'])
    spans: ResultSet = soup.find_all(tag)

    quant: List[float] = []
    unit: List[str] = []
    name: List[str] = []

    elem: Tag
    c = 0
    row = ['', '', '']
    for elem in spans:
        # for i, key in enumerate(['data-ingredient-quantity', 'data-ingredient-unit', 'data-ingredient-name']):
        if len(elem.attrs) > 0:
            for res in elem.attrs.keys():
                if res == 'class':
                    clss = elem.attrs.get(res)

                    if 'amount' in clss[0]:
                        quant.append(elem.text)
                        row[0] = elem.text
                    elif 'unit' in clss[0]:
                        unit.append(elem.text)
                        row[1] = elem.text
                    elif 'name' in clss[0]:
                        name.append(elem.text)
                        row[2] = elem.text
                        ingredients.loc[c] = row
                        row = ['', '', '']
                        c += 1
                if 'ingredient' in res:
                    if 'quantity' in res:
                        quant.append(elem.text)
                        row[0] = elem.text
                    elif 'unit' in res:
                        unit.append(elem.text)
                        row[1] = elem.text
                    elif 'name' in res:
                        name.append(elem.text)
                        row[2] = elem.text
                        ingredients.loc[c] = row
                        c += 1

    return ingredients

def parse_html(soup: BeautifulSoup, tag: str) -> pd.DataFrame:
    """ Extracts useful information from the parsed HTML.

    Args:
        html (BeautifulSoup): HTML file that has been received and parsed by BeautifulSoup

    Returns:
        pd.DataFrame: DataFrame that was constructed and formatted from html data
    """
    patches = [
        {
            "name": "",
            "date": "",
            
        }
    ]
    
    spans: ResultSet = soup.find_all(tag)
    for elem in spans:
        # for i, key in enumerate(['data-ingredient-quantity', 'data-ingredient-unit', 'data-ingredient-name']):
        if len(elem.attrs) > 0:
            for res in elem.attrs.keys():
                if res == 'class':
                    clss = elem.attrs.get(res)
                    val = elem.text
                    if clss == "PatchNotes-patchTitle"
    # https://overwatch.blizzard.com/en-us/news/patch-notes/
    # body
        # main
            # blz-section class="PatchNotesBody"
                # div class="PatchNotes-list"
                    # div class="PatchNotes-body"
                    # NOTE: This section contains the list of patches
                        # div class="PatchNotes-path PatchNotes-live"
                        # NOTE: This section contains the important info on each patch
                            # h3 class="PatchNotes-patchTitle"
    title = "Overwatch 2 Retail Patch Notes - July 12, 2024".split(" - ")
    name = title[0]
    date = datetime.datetime.strptime(title[1], "%B %d, %Y")
                            # div class="PatchNotes-section PatchNotes-section-hero_update"
                                # h4 class="PatchNotes-sectionTitle"
    role = "Tank"
    print(name, date, role)
                                    # div class="PatchNotesHeroUpdate"
                                        # div class="PatchNotesHeroUpdate-header"
                                            # h5 class="PatchNotesHeroUpdate-name"
    hero = "Ramattra"
                                            # div class="PatchNotesHeroUpdate-body"
                                                # div class="PatchNotesHeroUpdate-abilitiesList"
                                                    # div class="PatchNotesAbilityUpdate"
                                                        # div class="PatchNotesAbilityUpdate-name"
    ability = "Nemesis Form"
                                                        # div class="PatchNotesAbilityUpdate-detailList"
                                                            # ul
                                                                # li (changes)
    changes = [
        "Cooldown increased from 7 to 8 seconds.",
        "Base armor reduced from 100 to 75.",
        "Base health reduced from 275 to 250."
    ]


def parse_table(soup: BeautifulSoup) -> pd.DataFrame:
    """ Scrapes a table from the webpage into a pandas dataframe

    Args:
        html (BeautifulSoup): HTML file that has been received and parsed by BeautifulSoup

    Returns:
        pd.DataFrame: DataFrame that was constructed and formatted from the table
    """
    tbl = soup.find("table")
    df = pd.read_html(str(tbl))[0]

    return df



if __name__ == "__main__":
    URL = "https://overwatch.blizzard.com/en-us/news/patch-notes/"
    HTML = scrape_website(url=URL)
    db = parse_html(soup=HTML, tag=['script'])
    # db.to_csv(path_or_buf=f"{RTDIR}/groceries.csv", index=False, header=False)
    # db = parse_table(soup=HTML)
    print(db)
