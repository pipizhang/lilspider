# -*- coding: utf-8 -*-
from typing import List
from .base import MExcluded, MIncluded
from .dictionary import DictionaryChecker
from ..utils.html import get_soup

class LinkChecker(DictionaryChecker):
    """ Checker class for links url """
    name  = 'LinkChecker'
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

class LinkTextChecker(DictionaryChecker):
    """ Checker class for links text """
    name  = 'LinkTextChecker'
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

class TitleTextChecker(DictionaryChecker):
    """ Checker class for title text """
    name  = 'TitleTextChecker'
    dicts = [
        '产品', '推广'
    ]

    def run(self) -> None:
        MExcluded(self.dicts, self.example).run()

class CityIncludedChecker(DictionaryChecker):
    name = "CityIncludedChecker"

    def run(self) -> None:
        self.read_dict_file('zh_city')
        if not any(city in self.example for city in self.dicts):
            self.throw('CityIncludedChecker invalid "{}"'.format(self.example))

class CityExcludedChecker(DictionaryChecker):
    name = "CityExcludedChecker"

    def run(self) -> None:
        self.read_dict_file('zh_city')
        if any(city in self.example for city in self.dicts):
            self.throw('CityExcludedChecker invalid "{}"'.format(self.example))

