# -*- coding: utf-8 -*-
from typing import List
from .base import MExcluded
from .dictionary import Dictionary
from ..utils.html import get_soup

class Link(Dictionary):
    name = 'LinkChecker'
    dicts = [
        '.me', '.cc', '.info',
        '.taobao.com', 'jd.com'
    ]

    def run(self) -> None:
        soup = get_soup(self.example)
        els  = soup.find_all('a', href=True)
        if len(els) < 1:
            return
        for a in els:
            MExcluded(self.dicts, a['href']).run()

class LinkText(Dictionary):
    name = 'LinkTextChecker'
    dicts = [
        '手机话费', '网址导航'
    ]

    def run(self) -> None:
        soup = get_soup(self.example)
        els  = soup.find_all('a', href=True)
        if len(els) < 1:
            return
        for a in els:
            MExcluded(self.dicts, a.text).run()

class TitleText(Dictionary):
    name = 'TitleTextChecker'
    dicts = [
        '产品', '推广'
    ]

    def run(self) -> None:
        MExcluded(self.dicts, self.example).run()

class City(Dictionary):
    pass

