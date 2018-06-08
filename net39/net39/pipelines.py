# -*- coding: utf-8 -*-
import re
import datetime
import scrapy
from typing import Any, List
from lilspider.cleaner import HtmlCleaner

class ArticlePipeline(object):
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider) -> List:
        self._title(item)
        self._content(item)
        item['provider'] = spider.provider
        item['created_at'] = datetime.datetime.utcnow()
        item['updated_at'] = None
        item['indexed_at'] = None
        return item

    def _title(self, item: Any) -> None:
        item['title'] = item['title']

    def _content(self, item: Any) -> None:
        item['content'] = item['content']


