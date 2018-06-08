# -*- coding: utf-8 -*-
import re
from typing import Generator, List
from scrapy import Request, Selector
from scrapy.http import Response
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor as sle
from lilspider.spiders import SimpleSpider
from ..itemloaders import BlogItemLoader

class BlogSpider(SimpleSpider):
    name = 'blog'
    provider = 'blog.39.net'
    allowed_domains = ['blog.39.net']

    def __init__(self) -> None:
        pass

    def start_requests(self) -> Generator:
        urls = [
            #'http://blog.39.net/%E6%9F%AF%E4%BA%91%E8%B7%AF/a_9415456.html'
            'http://blog.39.net/liguangren/a_16681950.html'
        ]

        for url in urls:
            yield Request(url=url, callback=self.parseArticle)

    def parseArticle(self, response: Response) -> Generator:
        l = BlogItemLoader(response=response)
        l.add_xpath('title', '//div[@class="main_content"]//h1/text()')
        l.add_xpath('content', '//div[@id="main_body"]/node()')
        l.add_value('url', response.url)

        return l.load_item()

