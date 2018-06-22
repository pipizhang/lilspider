# -*- coding: utf-8 -*-
import re
from typing import List

class TextCleaner(object):
    def __init__(self, example: str, patterns: List=[]) -> None:
        self.example = example
        self.patterns = patterns

    def add_pattern(self, regex: str) -> None:
        self.patterns.append(regex)

    def run(self) -> str:
        if len(self.patterns) < 1: return self.example
        for p in self.patterns:
            self.example = re.sub(p, '', self.example, flags=re.M)
        return self.example

class HtmlInnertextCleaner(object):
    html_tag = 'p'

    def __init__(self, example: str, patterns: List=[]) -> None:
        self.example = example
        self.patterns = patterns
        self.re_tag = r'<' + self.html_tag + r'>.*?</' + self.html_tag + r'>'

    def add_pattern(self, regex: str, max_length: int=100, min_length: int=0) -> None:
        self.patterns.append({'regex': regex, 'max_length': max_length, 'min_length': min_length})

    def run(self) -> str:
        if len(self.patterns) < 1: return self.example
        rlist = []
        for p in self.patterns:
            for m in re.compile(self.re_tag, re.S).findall(self.example):
                if len(m) > p['min_length'] and len(m) < p['max_length'] and re.match(p['regex'], m):
                    rlist.append(m)

        #print(rlist)
        for r in rlist:
            self.example = self.example.replace(r, '')

        self.example = re.sub(r'^\n+', '', self.example, flags=re.M)
        return self.example

class PTextCleaner(HtmlInnertextCleaner):
    html_tag = 'p'

class DivTextCleaner(HtmlInnertextCleaner):
    html_tag = 'div'


