# -*- coding: utf-8 -*-
import re
from typing import List, Any
from bs4 import BeautifulSoup as bs
from ..cleaner import HtmlCleaner

def get_cleaner(shtml: str='') -> HtmlCleaner:
    return HtmlCleaner(shtml)

def get_soup(shtml: str='', **kwargs: str) -> bs:
    if len(kwargs):
        return bs(shtml, **kwargs)
    else:
        return bs(shtml, 'html.parser')

def pretty(shtml:str, newline_tags: Any=[], ltrim: bool=True, itrim: bool=True) -> str:
    soup = bs(shtml, 'html.parser')
    phtml = soup.prettify()

    if phtml[:5] == '<div>' and phtml[-6:] == '</div>':
        phtml = phtml[5:-6]

    phtml = remove_empty_elements(phtml)

    if itrim:
        phtml = inner_trim(phtml)

    phtml = re.sub(r'\n', '', phtml)

    if type(newline_tags) == str:
        newline_tags = newline_tags.split()
    if len(newline_tags):
        for tag in newline_tags:
            phtml = re.sub(r'\<\/'+re.escape(tag)+r'\>', f'</{tag}>\n', phtml)

    if ltrim:
        phtml = re.sub(r'^\s+', '', phtml, flags=re.MULTILINE)

    return phtml.strip()

def remove_empty_elements(shtml: str, keep_image: bool=True) -> str:
    soup = bs(shtml, "html.parser")
    for x in soup.find_all():
        if keep_image and x.name == 'img': continue
        if len(x.text.strip()) == 0 and (keep_image and not x.find_all('img')):
            x.extract()
    return str(soup)

def remove_tags(shtml: str) -> str:
    cleantext = bs(shtml, "lxml").text
    return cleantext.strip()

def inner_trim(shtml: str, tags: List=[]) -> str:
    if len(tags) == 0:
        tags = 'div p span strong'.split()
    re_tags = '|'.join(tags)

    phtml = re.sub(r'('+re_tags +r')>\s+', r'\g<1>>', shtml)
    phtml = re.sub(r'\s+</('+re_tags+r')>', r'</\g<1>>', phtml)
    return phtml

