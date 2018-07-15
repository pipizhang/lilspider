# -*- coding: utf-8 -*-
import re
import datetime
import scrapy
from typing import Any, List
from scrapy.exceptions import DropItem
from lilspider.cleaner import HtmlCleaner
from lilspider.utils.html import html2text

class ArticlePipeline(object):
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider) -> List:
        self._title(item)
        self._content(item)
        item['provider'] = spider.provider
        item['consumer'] = ''
        item['created_at'] = datetime.datetime.utcnow()
        item['updated_at'] = None
        item['indexed_at'] = None
        return item

    def _title(self, item: Any) -> None:
        if len(item['title']) < 3:
            raise DropItem("Drop item as title '{}' is bad".format(item['title']))
        item['title'] = item['title']

    def _content(self, item: Any) -> None:
        if len(html2text(item['content'])) < 200:
            raise DropItem("Drop item as content is too short")
        item['content'] = item['content']


