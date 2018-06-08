# -*- coding: utf-8 -*-
from scrapy.http import Response
from scrapy.spiders import CrawlSpider as cSpider

class CrawlSpider(cSpider):

    provider = ''

    def _extract_item(self, mode: str, resp: Response, rule: str, first: bool, join: bool, trim: bool) -> str:
        func = getattr(resp, mode)
        sele = func(rule)
        extracted = sele.extract_first() if first else sele.extract()
        if join:
            extracted = ''.join(extracted)
        if trim:
            extracted = extracted.strip()
        return extracted

    def extract_css(self, resp: Response, rule: str, first: bool=False, join: bool=True, trim: bool=True) -> str:
        return self._extract_item('css', resp,
            rule = rule,
            first = first,
            join = join,
            trim = trim
        )

    def extract_xpath(self, resp: Response, rule: str, first: bool=False, join: bool=True, trim: bool=True) -> str:
        return self._extract_item('xpath', resp,
            rule = rule,
            first = first,
            join = join,
            trim = trim
        )

