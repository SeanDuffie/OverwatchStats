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

class Hero:
    role = ""
    name = ""
    abilities = {}

class Patch:
    name = ""
    date = ""
    heroes: List[Hero] = []

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


def parse_html(soup: BeautifulSoup, tag: str) -> pd.DataFrame:
    """ Extracts useful information from the parsed HTML.

    Args:
        html (BeautifulSoup): HTML file that has been received and parsed by BeautifulSoup

    Returns:
        pd.DataFrame: DataFrame that was constructed and formatted from html data
    """
    spans: ResultSet = soup.find_all(tag)
    for elem in spans:
        # for i, key in enumerate(['data-ingredient-quantity', 'data-ingredient-unit', 'data-ingredient-name']):
        if len(elem.attrs) > 0:
            for res in elem.attrs.keys():
                if res == 'class':
                    clss = elem.attrs.get(res)
                    val = elem.text
                    print(f"{clss} | {val}")
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
                    if clss == "PatchNotes-patchTitle":
                        # title = "Overwatch 2 Retail Patch Notes - July 12, 2024".split(" - ")
                        title = val
                        name = title[0]
                        date = datetime.datetime.strptime(title[1], "%B %d, %Y")
                            # div class="PatchNotes-section PatchNotes-section-hero_update"
                                # h4 class="PatchNotes-sectionTitle"
                        print(f"Running patch {name} from {date}")
                    elif clss == "PatchNotes-sectionTitle":
                        # role = "Tank"
                        role = val
                        print(f"Roles: {role}")
                                    # div class="PatchNotesHeroUpdate"
                                        # div class="PatchNotesHeroUpdate-header"
                                            # h5 class="PatchNotesHeroUpdate-name"
                    elif clss == "PatchNotesHeroUpdate-name":
                        # hero = "Ramattra"
                        hero = val
                        print(f"\tCurrent Hero: {hero}")
                                            # div class="PatchNotesHeroUpdate-body"
                                                # div class="PatchNotesHeroUpdate-abilitiesList"
                                                    # div class="PatchNotesAbilityUpdate"
                                                        # div class="PatchNotesAbilityUpdate-name"
                    elif clss == "PatchNotesAbilityUpdate-name":
                        # ability = "Nemesis Form"
                        ability = val
                        print(f"\t\tCurrent Ability: {ability}")
                                                        # div class="PatchNotesAbilityUpdate-detailList"
                                                            # ul
                                                                # li (changes)
                    elif clss == "PatchNotesAbilityUpdate-detailList":
                        # changes = [
                        #     "Cooldown increased from 7 to 8 seconds.",
                        #     "Base armor reduced from 100 to 75.",
                        #     "Base health reduced from 275 to 250."
                        # ]
                        changes = val
                        print(f"\t\t\tChanges: {changes}")
                else:
                    print(res)
        # else:
        #     print("Error! No attrs")

from lxml import html

def parse_xpth(url: str):
    # Perform the request
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers, timeout=10)

    # Check if the HTTP request was successful
    assert response.status_code == 200

    tree: html.HtmlElement = html.fromstring(response.content)
    elements: List[html.HtmlElement] = tree.xpath("/html/body/main/blz-section/div[@class='PatchNotes-list']/div[@class='PatchNotes-body']/div[@class='PatchNotes-patch PatchNotes-live']")
    for elem in elements:
        print(elem.attrib['class'])
        # print(elem.)
        titles: List[html.HtmlElement] = elem.xpath("h3[@class='PatchNotes-patchTitle']")
        for title in titles:
            print(f"Patch: {title.text}")
            split_title = title.text.split(" - ")
            # name = split_title[0]
            # date = datetime.datetime.strptime(split_title[1], "%B %d, %Y")
            sections: List[html.HtmlElement] = elem.xpath("div[@class='PatchNotes-section PatchNotes-section-hero_update']")
            for section in sections:
                print(f"\t{section.text}")
                roles: List[html.HtmlElement] = section.xpath("div/div[@class='PatchNotes-section PatchNotes-section-generic_update']")
                for role in roles:
                    print(f"\t\t{role.append("h4").text}")
                    heroes: List[html.HtmlElement] = role.xpath("")
                    for hero in heroes:
                        print(hero.text)

    # # https://overwatch.blizzard.com/en-us/news/patch-notes/
    # # html/body/main/blz-section class="PatchNotesBody"/div class="PatchNotes-list"/div class="PatchNotes-body"/div class="PatchNotes-path PatchNotes-live"
    # # NOTE: This section contains the important info on each patch
        # # h3 class="PatchNotes-patchTitle"
        # # div class="PatchNotes-section PatchNotes-section-hero_update"
            # # h4 class="PatchNotes-sectionTitle"
            # # div class="PatchNotesHeroUpdate"/div class="PatchNotesHeroUpdate-header"
                    # # h5 class="PatchNotesHeroUpdate-name"
                    # # div class="PatchNotesHeroUpdate-body"/div class="PatchNotesHeroUpdate-abilitiesList"/div class="PatchNotesAbilityUpdate"
                        # # div class="PatchNotesAbilityUpdate-name"
                        # # div class="PatchNotesAbilityUpdate-detailList"/ul/li (changes)


if __name__ == "__main__":
    URL = "https://overwatch.blizzard.com/en-us/news/patch-notes/"
    # HTML = scrape_website(url=URL)
    # parse_html(soup=HTML, tag=['script'])
    parse_xpth(URL)
    # db.to_csv(path_or_buf=f"{RTDIR}/groceries.csv", index=False, header=False)
    # db = parse_table(soup=HTML)
    # print(db)
