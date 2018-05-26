# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from ..cleaner import HtmlCleaner

def get_cleaner() -> HtmlCleaner:
    return HtmlCleaner()

def pretty(shtml) -> str:
    soup = bs(shtml, "html.parser")
    phtml = soup.prettify()
    if phtml[:5] == '<div>' and phtml[-6:] == '</div>':
        phtml = phtml[5:-6]
    return phtml.strip()

def remove_empty_elements(shtml: str) -> str:
    soup = bs(shtml, "html.parser")
    for x in soup.find_all():
        if len(x.text.strip()) == 0:
            x.extract()
    return str(soup)
