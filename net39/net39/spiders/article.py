# -*- coding: utf-8 -*-
import re
import random
from typing import Generator, List
from scrapy.http import Response
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from lilspider.spiders import CrawlSpider
from ..items import ArticleItem
from ..itemloaders import ArticleItemLoader

class ArticleSpider(CrawlSpider):
    name = 'article'
    provider = '39.net'
    allowed_domains = ['39.net']
    disallowed_domains = [
        'drug.39.net',
        'qx.39.net',
        'zx.39.net',
        'aids.39.net',
        'zl.39.net',
    ]
    start_urls = [random.choice([
        'http://care.39.net/a/20111031/1834407.html'
        #'http://disease.39.net/',
        #'http://woman.39.net/',
        #'http://oldman.39.net/',
        #'http://baby.39.net/',
        #'http://care.39.net/',
    ])]
    rules = [
        Rule(LinkExtractor(allow=(r'http:\/\/[a-z]+\.39\.net\/a\/\d+\/\d+\.html$')), callback='parse_article', follow=True),
    ]
    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    def parse_article(self, response: Response) -> Generator:
        l = ArticleItemLoader(response=response)
        l.add_css('title', 'div.art_box h1::text')
        l.add_css('content', 'div#contentText > *')
        l.add_value('url', response.url)

        return l.load_item()

