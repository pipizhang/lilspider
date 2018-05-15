# -*- coding: utf-8 -*-
import re
from typing import Generator, List

from scrapy import Request, Selector
from scrapy.http import Response
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor as sle
from ..items import BaiduItem

from lilspider.spiders import CommonSpider 
class SearchSpider(CommonSpider):
    name = 'search'
    allowed_domains = ['www.baidu.com']

    def __init__(self) -> None:
        pass

    def start_requests(self) -> Generator:
        urls = [
            'https://www.baidu.com/s?ie=utf-8&wd=blog.39.net+%E8%83%83%E7%97%85'
        ]

        for url in urls:
            yield Request(url=url, callback=self.parseSearch)

    def parseSearch(self, response: Response) -> Generator:
        for item in self.getItems(response):
            yield item

        for page in self.getPages(response):
            yield Request(url=page, callback=self.parseSearch)

    def getItems(self, response: Response) -> List[BaiduItem]:
        items = []
        els = response.xpath('//div[contains(@class, "c-container")]')
        for el in els:
            title = ''.join(el.xpath('.//h3/a//text()').extract()).strip()
            url = ''.join(el.xpath('.//a[@class="c-showurl"]//@href').extract()).strip()
            showurl = ''.join(el.xpath('.//a[@class="c-showurl"]//text()').extract()).strip()
            item = BaiduItem()
            item['url'] = url
            item['showurl'] = showurl
            item['title'] = title
            item['site'] = 'baidu'
            items.append(item)
        return items

    def getPages(self, response: Response) -> List[str]:
        pages = []
        p = re.compile("wd=.*pn=(\d+)&")
        #els = response.css('#page a::attr(href)')
        els = response.xpath('//div[@id="page"]//a/@href')

        for el in els:
            tmp  = el.extract()
            if p.search(tmp) != None:
                page_num = int(p.search(tmp).group(1))
                if page_num > 10 and page_num <=20:
                    url = 'https://www.baidu.com/s?ie=urf-8&wd=blog.39.net+%E8%83%83%E7%97%85&pn={}'.format(page_num)
                    pages.append(url)

        return pages

