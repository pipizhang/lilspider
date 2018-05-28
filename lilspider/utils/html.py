# -*- coding: utf-8 -*-
import re
from typing import List, Any
from bs4 import BeautifulSoup as bs
from ..cleaner import HtmlCleaner

def get_cleaner(shtml: str='') -> HtmlCleaner:
    return HtmlCleaner(shtml)

def pretty(shtml:str, newline_tags: Any=[], ltrim: bool=True) -> str:
    soup = bs(shtml, 'html.parser')
    phtml = soup.prettify()

    if phtml[:5] == '<div>' and phtml[-6:] == '</div>':
        phtml = phtml[5:-6]

    phtml = remove_empty_elements(phtml)
    phtml = re.sub(r'\n', '', phtml)

    if type(newline_tags) == str:
        newline_tags = newline_tags.split()
    if len(newline_tags):
        for tag in newline_tags:
            phtml = re.sub(r'\<\/'+re.escape(tag)+r'\>', '</{}>\n'.format(tag), phtml)

    if ltrim:
        phtml = re.sub(r'^\s+', '', phtml, flags=re.MULTILINE)

    return phtml.strip()

def remove_empty_elements(shtml: str) -> str:
    soup = bs(shtml, "html.parser")
    for x in soup.find_all():
        if len(x.text.strip()) == 0:
            x.extract()
    return str(soup)

def remove_tags(shtml: str) -> str:
    cleantext = bs(shtml, "lxml").text
    return cleantext.strip()

